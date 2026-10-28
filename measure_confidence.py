"""Reproduce saved trials to measure criterion 5 without changing training.

Run with the project interpreter. Each trial uses a fresh process to release
GPU memory. Original result files are read and never overwritten.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def trial(phase, seed):
    notebook = json.loads((ROOT / 'takemeter.ipynb').read_text())
    ns = {}
    for i in (2, 6, 8, 12, 14, 16):
        source = ''.join(notebook['cells'][i]['source'])
        if i == 14:
            source = source.split('\ntrainer, tokenizer = train_model(')[0]
        if i == 16:
            source = source.split('\nresults = evaluate(')[0]
        exec(compile(source, f'notebook_cell_{i}', 'exec'), ns)
    ns['MAX_LENGTH'] = 128 if phase == 'before' else 256
    tr, va, te = ns['split_dataset'](ns['df'], seed)
    trainer, tokenizer = ns['train_model'](
        tr, va, ns['LABELS'], seed, ns['EPOCHS'], ns['LEARNING_RATE'],
        ns['BATCH_SIZE'], ns['BASE_MODEL'], quiet=True,
    )
    result = ns['evaluate'](trainer, tokenizer, te, ns['LABELS'], seed=seed)
    originals = json.loads((ROOT / f'results_three_seeds_{phase}.json').read_text())
    original = next(r for r in originals if r['seed'] == seed)
    matched = all(result[k] == original[k] for k in ('accuracy', 'confusion', 'per_label'))
    return {
        'phase': phase, 'seed': seed, 'max_length': ns['MAX_LENGTH'],
        'device': ns['DEVICE'], 'device_name': ns['DEVICE_NAME'],
        'torch_version': ns['torch'].__version__,
        'matches_original_discrete_metrics': matched,
        'accuracy': result['accuracy'], 'confidence': result['confidence'],
    }


if __name__ == '__main__':
    if len(sys.argv) == 3:
        phase, seed = sys.argv[1], int(sys.argv[2])
        result = trial(phase, seed)
        output = ROOT / f'confidence_{phase}_{seed}.json'
        output.write_text(json.dumps(result, indent=2) + '\n')
        print(f'Saved {output.name}', flush=True)
    else:
        measurements = []
        for phase in ('before', 'after'):
            for seed in (42, 7, 2024):
                subprocess.run([sys.executable, __file__, phase, str(seed)], cwd=ROOT, check=True)
                path = ROOT / f'confidence_{phase}_{seed}.json'
                measurements.append(json.loads(path.read_text()))
        (ROOT / 'confidence_threshold_results.json').write_text(
            json.dumps(measurements, indent=2) + '\n'
        )
        print('Saved all six confidence measurements.', flush=True)
