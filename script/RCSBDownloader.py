import urllib.request
from pathlib import Path


def fetch_pdb_id(pdb_id_file):
    pdb_ids = []

    # read file
    with open(pdb_id_file, 'r') as f:
        for line in f:
            if line.strip():
                pdb_ids.append(line.strip())

    return pdb_ids


def get_protein_files(pdb_ids, output_dir, format):
    """
    :param pdb_ids: list pdb ids
    :param output_dir: str output directory
    :param format: str 'pdb' or 'fasta'
    """

    # PDB ids that failed to download are stored here.
    fail = []
    # download proteins Files
    for pdb_id in pdb_ids:
        # Checks if the protein file with the corresponding format exists in the output directory.
        protein_file = Path(output_dir + '/' + pdb_id + '.' + format)
        if protein_file.exists():
            print("File" + pdb_id + "." + format + " was in the " + output_dir +
                  "directory, which is why it didn't download again!")
        else:
            try:
                if format == 'pdb':
                    urllib.request.urlretrieve('https://files.rcsb.org/download/' + pdb_id + '.pdb',
                                               output_dir + '/' + pdb_id + '.pdb')
                elif format == 'fasta':
                    urllib.request.urlretrieve('https://www.rcsb.org/fasta/entry/' + pdb_id + '.fasta',
                                               output_dir + '/' + pdb_id + '.fasta')
                else:
                    print("invalid format")

            except "Fail to download protein file":
                fail.append(pdb_id)

    if fail:
        print("The download of some PDB ids failed!")
        for pdb_id in fail:
            print(pdb_id)
    else:
        print("Download of all " + format + " files has been completed!")


if __name__ == '__main__':
    # input file
    # include pdb ids
    input_file = '../input/rcsb_sample.pdbid.list'

    # output dir to store PDB files
    pdb_output_dir = '../output/rcsb/pdb'
    # output dir to store fasta files
    fasta_output_dir = '../output/rcsb/fasta'

    # getch pdb ids
    pdb_ids = fetch_pdb_id(input_file)
    # get pdb files
    get_protein_files(pdb_ids, pdb_output_dir, 'pdb')
    # get fasta files
    get_protein_files(pdb_ids, fasta_output_dir, 'fasta')


