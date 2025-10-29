# EE623 Assignment 1: Acoustic Analysis of Hindi Sounds

## Author

Mehul Bharti (220108036)

## Overview

This repository contains the work for Assignment 1 of the EE623 course. The assignment involves recording and analyzing the acoustic properties of selected Hindi vowels and consonants based on their place and manner of articulation.

## Objectives

1.  *Spectrogram and AMDF Analysis:*
    * Compute narrow-band spectrograms to determine pitch (F0).
    * Verify pitch using the Average Magnitude Difference (AMD) function via a Python script.
    * Compute wideband spectrograms and use Praat to identify and mark formant contours (F1, F2, F3), focusing on formant transitions for consonants.
2.  *Cepstral Analysis (Vowels Only):*
    * Estimate the average pitch (F0) and average formant frequencies (F1, F2, F3) over at least 6 consecutive frames using cepstral analysis implemented in Python.
    * Generate framewise plots of the cepstrally smoothed spectrum and the cepstral sequence.

## Language and Sounds Analyzed

* *Language:* Hindi
* *Vowels:* /i/ (ई), /u/ (उ), /a/ (अ), /e/ (ए), /o/ (ओ)
* *Voiced Consonants:* /ga/ (ग), /dʒa/ (ज), /ɖa/ (ड), /da/ (द), /ba/ (ब)

## Tools Used

* *Recording & Initial Analysis:* Audacity
* *Formant Tracking:* Praat
* *Pitch Verification (AMD) & Cepstral Analysis:* Python 3 (using libraries: numpy, scipy, matplotlib, librosa)
