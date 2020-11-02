__author__ = 'Brian M Anderson'
# Created on 10/28/2020

from DicomRTTool import DicomReaderWriter, plot_scroll_Image, np, sitk, os
from Resample_Class.src.NiftiResampler.ResampleTools import Resample_Class_Object, sitk

'''
Resampler class to make it into a 512x512xcorrect thickness
'''
resampler = Resample_Class_Object()


MRN = 'some_number'
path = r'Z:\Carlo rCBV Files\Tumor and White Matter\{}\Pre\Tumor_RayStation_Export'.format(MRN)

'''
This will load up the T1C and mask named GTV_training
'''
reader = DicomReaderWriter(get_images_mask=True, Contour_Names=['GTV_training'],
                           require_all_contours=False)

reader.down_folder(path)

MR_numpy_array = reader.ArrayDicom
tumor_numpy_array = reader.mask
# Save them as .nii files
sitk.WriteImage(reader.annotation_handle, os.path.join(path, 'tumor_mask.nii'))
sitk.WriteImage(reader.dicom_handle, os.path.join(path, 'T1_plus_c_Image.nii'))

'''
Now load up the Perfusion image
'''
path = r'Z:\Carlo rCBV Files\Tumor and White Matter\{}\Pre\Perfusion_Raystation_Export'.format(MRN)
reader_perfusion = DicomReaderWriter(get_images_mask=True)
reader_perfusion.down_folder(path)
perfusion = reader_perfusion.ArrayDicom


perfusion_handle = reader_perfusion.dicom_handle
tumor_handle = reader.dicom_handle
'''
Resample to have the tumor_handle's spacing
'''
resampled_perfusion = resampler.resample_image(perfusion_handle, output_spacing=tumor_handle.GetSpacing())
sitk.WriteImage(resampled_perfusion, os.path.join(path, 'resampled_perfusion.nii'))
