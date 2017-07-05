from django.shortcuts import redirect, render, get_object_or_404
from .forms import dnaForm
from .models import dna



def first_page(request):
    if request.method == "POST":
        form = dnaForm(request.POST)
        if form.is_valid():
            new_dna = form.save(commit=False)
            new_dna.save()
            return redirect('final', pk=new_dna.pk)
    else:
        form = dnaForm()
    return render(request, 'converter/first_page.html', {'form': form})


#@render_to('converter:output.html')
def final(request, pk):
    sequ = get_object_or_404(dna, pk=pk)
    seq = str(sequ)
    seq = seq.upper()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    seq = seq.replace(" ", "")

    def translate(sequence):

        #sequence = sequence.upper()
        table = {
            'ATA': 'Isoleucine', 'ATC': 'Isoleucine', 'ATT': 'Isoleucine', 'ATG': 'Methionine',
            'ACA': 'Threonine', 'ACC': 'Threonine', 'ACG': 'Threonine', 'ACT': 'Threonine',
            'AAC': 'Asparagine', 'AAT': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine',
            'AGC': 'Serine', 'AGT': 'Serine', 'AGA': 'Arginine', 'AGG': 'Arginine',
            'CTA': 'Leucine', 'CTC': 'Leucine', 'CTG': 'Leucine', 'CTT': 'Leucine',
            'CCA': 'Proline', 'CCC': 'Proline', 'CCG': 'Proline', 'CCT': 'Proline',
            'CAC': 'Histidine', 'CAT': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine',
            'CGA': 'Arginine', 'CGC': 'Arginine', 'CGG': 'Arginine', 'CGT': 'Arginine',
            'GTA': 'Valine', 'GTC': 'Valine', 'GTG': 'Valine', 'GTT': 'Valine',
            'GCA': 'Alanine', 'GCC': 'Alanine', 'GCG': 'Alanine', 'GCT': 'Alanine',
            'GAC': 'Aspartic Acid', 'GAT': 'Aspartic Acid', 'GAA': 'Glutamic Acid', 'GAG': 'Glutamic Acid',
            'GGA': 'Glycine', 'GGC': 'Glycine', 'GGG': 'Glycine', 'GGT': 'Glycine',
            'TCA': 'Serine', 'TCC': 'Serine', 'TCG': 'Serine', 'TCT': 'Serine',
            'TTC': 'Phenylalanine', 'TTT': 'Phenylalanine', 'TTA': 'Leucine', 'TTG': 'Leucine',
            'TAC': 'Tyrosine', 'TAT': 'Tyrosine', 'TAA': '_', 'TAG': '_',
            'TGC': 'Cysteine', 'TGT': 'Cysteine', 'TGA': '_', 'TGG': 'Tryptophan',
        }
        protein = " "
        #if len(sequence) % 3 == 0:
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i + 3]
            if len(codon) < 3:
                protein += 'The END'
                return protein
            if table[codon] == '_':
                return protein
            protein += table[codon]
            protein += '->'
        protein += 'The END'
        return protein

    start = seq.find('ATG')
    dnaa = seq[start:]
    prt = translate(dnaa)
    return render(request, 'converter/output.html', {'prt': prt})
