# coding: utf-8

""" Read and write potentials to text (YAML) files. """

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
import os

# Third-party
import astropy.units as u
import yaml

__all__ = ['read', 'write']

def from_dict(d):
    """
    Convert a dictionary potential specification into a
    :class:`~gary.potential.Potential` object.

    Parameters
    ----------
    d : dict
        Dictionary specification of a potential.

    """

    try:
        class_name = d['class']
    except KeyError:
        raise KeyError("Potential dictionary must contain a key 'class' for "
                       "specifying the name of the Potential class.")

    try:
        unitsys = [u.Unit(unit) for unit in d['units']]
    except KeyError:
        raise KeyError("Potential dictionary must contain a key 'units' with "
                       "a list of strings specifying the unit system.")

    if 'parameters' in d:
        params = d['parameters']
    else:
        params = dict()

    # Hack because PyYAML sux
    for k,v in params.items():
        params[k] = float(v)

    from .. import potential
    Potential = getattr(potential, class_name)

    return Potential(units=unitsys, **params)

def to_dict(potential):
    """
    Turn a potential object into a dictionary that fully specifies the
    state of the object.

    Parameters
    ----------
    potential :
        The instantiated :class:`~gary.potential.Potential` object.

    """
    d = dict()

    d['class'] = potential.__class__.__name__
    d['units'] = [str(unit) for unit in potential.units]
    if len(potential.parameters) > 0:
        d['parameters'] = potential.parameters

    return d

def read(f):
    """
    Read a potential specification file and return a
    :class:`~gary.potential.Potential` object instantiated with parameters
    specified in the spec file.

    Parameters
    ----------
    f : str, file_like
        A block of text, filename, or file-like object to parse and read
        a potential from.

    """
    try:
        with open(os.path.abspath(f)) as fil:
            p_dict = yaml.load(fil.read())
    except:
        p_dict = yaml.load(f)

    return from_dict(p_dict)

def write(potential, f):
    """
    Write a :class:`~gary.potential.Potential` object out to a text (YAML)
    file.

    Parameters
    ----------
    potential :
        The instantiated :class:`~gary.potential.Potential` object.
    f : str, file_like
        A filename or file-like object to write the input potential object to.

    """
    d = to_dict(potential)

    if hasattr(f, 'write'):
        yaml.dump(d, f, default_flow_style=False)
    else:
        with open(f, 'w') as f:
            yaml.dump(d, f, default_flow_style=False)
