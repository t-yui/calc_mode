#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np


def calc_mode(sample_list):
    """
    Calculate mode from continuous samples.

    Parameters
    ----------
    sample_list : list or numpy array

    Returns
    -------
    mode : float
    """
    hist_freqs = np.histogram(sample_list, bins="auto")[0]
    hist_edges = np.histogram(sample_list, bins="auto")[1]
    _left_edges = hist_edges[1:]
    _risght_edges = hist_edges[:-1]
    hist_mean = (_left_edges + _risght_edges) / 2
    mode_val = hist_mean[hist_freqs == max(hist_freqs)][0]
    return mode_val


if __name__=="__main__":
    samples = np.random.normal(2,1,1000)
    mode_val = calc_mode(sample_list=samples)
    print(mode_val)