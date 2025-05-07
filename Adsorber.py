from ase import Atoms
from ase.build import surface, add_adsorbate
from ase.visualize import view
from ase.io import read
import sys
from acat.adsorption_sites import SlabAdsorptionSites
from acat.build import add_adsorbate_to_site



# Load your adsorbate POSCAR
adsorbate = read('POSCAR_CCH3.vasp', format='vasp')

def add_to_sites_separately(adsorbate, target_site='hcp', height=3.5):
    # Load your NiCu surface POSCAR
    slab = read('POSCAR_clean.vasp', format='vasp')
    sas = SlabAdsorptionSites(slab, surface='fcc111')
    sites = sas.get_sites()
    print(sites)
    ad_sites = [s['site'] for s in sites if s['site'] == target_site]

    print('These are all the sites: \n', sites)

    for i in range(len(ad_sites)):
        slab = read('POSCAR_clean.vasp', format='vasp')
        sas = SlabAdsorptionSites(slab, surface='fcc111')
        sites = sas.get_sites()
        # TODO: Add the adsorbate to the site one at a time and view each one
        add_adsorbate_to_site(slab, adsorbate=adsorbate, site=site, height=height)

    
    for st in sites:
        if st['site'] == 'hcp':
            add_adsorbate_to_site(slab, adsorbate=adsorbate, site=st, height=3.0)
            break
    view(slab)


def print_sites(slab):
    sas = SlabAdsorptionSites(slab, surface='fcc111')
    sites = sas.get_sites()
    print(sites)


if __name__ == "__main__":
    # add_to_sites_separately(adsorbate, target_site='hcp', height=3.5)
    slab = read('POSCAR_clean.vasp', format='vasp')
    print_sites(slab)