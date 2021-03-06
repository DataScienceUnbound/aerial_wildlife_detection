'''
    Enum for all column names in the database tables.

    2019 Benjamin Kellenberger
'''

from enum import Enum

class FieldNames_prediction(Enum):
    labels = set(['label', 'confidence', 'priority'])
    points = set(['label', 'confidence','priority',  'x', 'y'])
    boundingBoxes = set(['label', 'confidence','priority',  'x', 'y', 'width', 'height'])
    segmentationMasks = set(['segmentationmask', 'priority', 'width', 'height'])

class FieldNames_annotation(Enum):
    labels = set(['meta', 'label', 'unsure'])
    points = set(['meta', 'label', 'x', 'y', 'unsure'])
    boundingBoxes = set(['meta', 'label', 'x', 'y', 'width', 'height', 'unsure'])
    segmentationMasks = set(['meta', 'segmentationmask', 'width', 'height'])