
EXP_NAMES = ['ground_truth', 'ground_truth_vocoded', 'pabc_cleaned_mini', 'pabc_cleaned_mini_v2', 'pabc_cleaned_mini_v3', 'pabc_cleaned_mini_v4', 'pabc_cleaned_mini_v5']
BASE_NAME = 'https://github.com/atliSig/IS_samples/blob/master/mos/'

def make_mos_urls(num_samples:int=30, out_path:str='./mos-urls.txt'):
    """
    Makes a file containing the urls of the MOS scores for each experiment.
    """
    with open(out_path, 'w') as f:
        for exp_name in EXP_NAMES:
            for i in range(num_samples):
                f.write(f'{BASE_NAME}{exp_name}/sample_{i}.wav?raw=true\n')

def make_axy_urls(num_samples:int=150, out_path:str='./axy-urls.txt'):
    """
    Makes a file containing the urls of the AXY scores for each experiment.
    """
    with open(out_path, 'w') as f:
        for i in range(num_samples):
            f.write(f'sample_{i}.wav?raw=true\n')


def make_mushra_urls(num_samples:int=60, out_path:str='./mushra-urls.txt'):
    """
    Makes a file containing the urls of the MUSHRA scores for each experiment.
    """
    with open(out_path, 'w') as f:
        for i in range(num_samples):
            f.write(f'sample_{i}.wav?raw=true\n')


make_mushra_urls()