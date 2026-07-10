# RCBV-Calculator

Preprocessing script for relative cerebral blood volume (rCBV) analysis of brain
tumors from MRI. It takes a RayStation DICOM export of a T1-post-contrast image with a
tumor contour plus a perfusion image, converts them to NIfTI, and resamples the
perfusion volume onto the tumor image's spacing so the two are voxel-aligned for
downstream rCBV computation.

One-off research script (created 2020-10-28), not a packaged tool. Input paths and the
patient MRN are hardcoded near the top of `Main.py` and must be edited before running.

## How it works (`Main.py`)

- Reads the T1+C DICOM series and the `GTV_training` contour with `DicomReaderWriter`,
  writing `tumor_mask.nii` and `T1_plus_c_Image.nii`.
- Reads the perfusion DICOM series.
- Resamples the perfusion image to the tumor image's spacing and writes
  `resampled_perfusion.nii`.

## Requirements

- Python with SimpleITK and NumPy
- [DicomRTTool](https://github.com/brianmanderson/DicomRTTool) for DICOM/contour reading
- `Resample_Class` (included as a git submodule) for resampling

Clone with submodules:

```
git clone --recurse-submodules https://github.com/brianmanderson/RCBV-Calculator.git
```

## Usage

Edit the `MRN` and path variables at the top of `Main.py`, then run:

```
python Main.py
```
