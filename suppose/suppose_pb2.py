# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: suppose.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='suppose.proto',
  package='suppose',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rsuppose.proto\x12\x07suppose\" \n\x08Vector2f\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"+\n\x08Vector3f\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"v\n\x06Pose2D\x12-\n\tkeypoints\x18\x01 \x03(\x0b\x32\x1a.suppose.Pose2D.Keypoint2D\x1a=\n\nKeypoint2D\x12 \n\x05point\x18\x01 \x01(\x0b\x32\x11.suppose.Vector2f\x12\r\n\x05score\x18\x02 \x01(\x02\"\xa2\x01\n\x11ReprojectedPose2D\x12\x43\n\tkeypoints\x18\x01 \x03(\x0b\x32\x30.suppose.ReprojectedPose2D.ReprojectedKeypoint2D\x1aH\n\x15ReprojectedKeypoint2D\x12 \n\x05point\x18\x01 \x01(\x0b\x32\x11.suppose.Vector2f\x12\r\n\x05\x65rror\x18\x02 \x01(\x02\"\x96\x01\n\x06Pose3D\x12\r\n\x05\x65rror\x18\x01 \x01(\x02\x12-\n\tkeypoints\x18\x02 \x03(\x0b\x32\x1a.suppose.Pose3D.Keypoint3D\x1aN\n\nKeypoint3D\x12 \n\x05point\x18\x01 \x01(\x0b\x32\x11.suppose.Vector3f\x12\x1e\n\x03std\x18\x02 \x01(\x0b\x32\x11.suppose.Vector3f\":\n\x05\x46rame\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x1e\n\x05poses\x18\x02 \x03(\x0b\x32\x0f.suppose.Pose2D\"<\n\x07\x46rame3D\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x1e\n\x05poses\x18\x02 \x03(\x0b\x32\x0f.suppose.Pose3D\"|\n\x0eProcessedVideo\x12\x0e\n\x06\x63\x61mera\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x0c\n\x04\x66ile\x18\x04 \x01(\t\x12\r\n\x05model\x18\x05 \x01(\t\x12\x1e\n\x06\x66rames\x18\x06 \x03(\x0b\x32\x0e.suppose.Frame\"G\n\x04Room\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x10processed_videos\x18\x02 \x03(\x0b\x32\x17.suppose.ProcessedVideo\"S\n\x10ProcessedVideo3D\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61meras\x18\x02 \x03(\t\x12 \n\x06\x66rames\x18\x03 \x03(\x0b\x32\x10.suppose.Frame3D\"#\n\x05Image\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x14\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x01(\t2\xac\x01\n\rPoseExtractor\x12+\n\x07GetPose\x12\x0e.suppose.Image\x1a\x0e.suppose.Frame\"\x00\x12\x33\n\x0bStreamPoses\x12\x0e.suppose.Image\x1a\x0e.suppose.Frame\"\x00(\x01\x30\x01\x12\x39\n\x14StreamPosesFromVideo\x12\r.suppose.File\x1a\x0e.suppose.Frame\"\x00\x30\x01\x62\x06proto3')
)




_VECTOR2F = _descriptor.Descriptor(
  name='Vector2f',
  full_name='suppose.Vector2f',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='suppose.Vector2f.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='suppose.Vector2f.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=58,
)


_VECTOR3F = _descriptor.Descriptor(
  name='Vector3f',
  full_name='suppose.Vector3f',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='suppose.Vector3f.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='suppose.Vector3f.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='suppose.Vector3f.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=103,
)


_POSE2D_KEYPOINT2D = _descriptor.Descriptor(
  name='Keypoint2D',
  full_name='suppose.Pose2D.Keypoint2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='suppose.Pose2D.Keypoint2D.point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='suppose.Pose2D.Keypoint2D.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=223,
)

_POSE2D = _descriptor.Descriptor(
  name='Pose2D',
  full_name='suppose.Pose2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='suppose.Pose2D.keypoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POSE2D_KEYPOINT2D, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=223,
)


_REPROJECTEDPOSE2D_REPROJECTEDKEYPOINT2D = _descriptor.Descriptor(
  name='ReprojectedKeypoint2D',
  full_name='suppose.ReprojectedPose2D.ReprojectedKeypoint2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='suppose.ReprojectedPose2D.ReprojectedKeypoint2D.point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='suppose.ReprojectedPose2D.ReprojectedKeypoint2D.error', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=388,
)

_REPROJECTEDPOSE2D = _descriptor.Descriptor(
  name='ReprojectedPose2D',
  full_name='suppose.ReprojectedPose2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='suppose.ReprojectedPose2D.keypoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPROJECTEDPOSE2D_REPROJECTEDKEYPOINT2D, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=388,
)


_POSE3D_KEYPOINT3D = _descriptor.Descriptor(
  name='Keypoint3D',
  full_name='suppose.Pose3D.Keypoint3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='suppose.Pose3D.Keypoint3D.point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='std', full_name='suppose.Pose3D.Keypoint3D.std', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=541,
)

_POSE3D = _descriptor.Descriptor(
  name='Pose3D',
  full_name='suppose.Pose3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='suppose.Pose3D.error', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='suppose.Pose3D.keypoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POSE3D_KEYPOINT3D, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=541,
)


_FRAME = _descriptor.Descriptor(
  name='Frame',
  full_name='suppose.Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='suppose.Frame.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poses', full_name='suppose.Frame.poses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=601,
)


_FRAME3D = _descriptor.Descriptor(
  name='Frame3D',
  full_name='suppose.Frame3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='suppose.Frame3D.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poses', full_name='suppose.Frame3D.poses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=663,
)


_PROCESSEDVIDEO = _descriptor.Descriptor(
  name='ProcessedVideo',
  full_name='suppose.ProcessedVideo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera', full_name='suppose.ProcessedVideo.camera', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='suppose.ProcessedVideo.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='suppose.ProcessedVideo.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='suppose.ProcessedVideo.file', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='suppose.ProcessedVideo.model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frames', full_name='suppose.ProcessedVideo.frames', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=789,
)


_ROOM = _descriptor.Descriptor(
  name='Room',
  full_name='suppose.Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='suppose.Room.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed_videos', full_name='suppose.Room.processed_videos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=791,
  serialized_end=862,
)


_PROCESSEDVIDEO3D = _descriptor.Descriptor(
  name='ProcessedVideo3D',
  full_name='suppose.ProcessedVideo3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room', full_name='suppose.ProcessedVideo3D.room', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cameras', full_name='suppose.ProcessedVideo3D.cameras', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frames', full_name='suppose.ProcessedVideo3D.frames', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=947,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='suppose.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='suppose.Image.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='suppose.Image.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=949,
  serialized_end=984,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='suppose.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='suppose.File.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=986,
  serialized_end=1006,
)

_POSE2D_KEYPOINT2D.fields_by_name['point'].message_type = _VECTOR2F
_POSE2D_KEYPOINT2D.containing_type = _POSE2D
_POSE2D.fields_by_name['keypoints'].message_type = _POSE2D_KEYPOINT2D
_REPROJECTEDPOSE2D_REPROJECTEDKEYPOINT2D.fields_by_name['point'].message_type = _VECTOR2F
_REPROJECTEDPOSE2D_REPROJECTEDKEYPOINT2D.containing_type = _REPROJECTEDPOSE2D
_REPROJECTEDPOSE2D.fields_by_name['keypoints'].message_type = _REPROJECTEDPOSE2D_REPROJECTEDKEYPOINT2D
_POSE3D_KEYPOINT3D.fields_by_name['point'].message_type = _VECTOR3F
_POSE3D_KEYPOINT3D.fields_by_name['std'].message_type = _VECTOR3F
_POSE3D_KEYPOINT3D.containing_type = _POSE3D
_POSE3D.fields_by_name['keypoints'].message_type = _POSE3D_KEYPOINT3D
_FRAME.fields_by_name['poses'].message_type = _POSE2D
_FRAME3D.fields_by_name['poses'].message_type = _POSE3D
_PROCESSEDVIDEO.fields_by_name['frames'].message_type = _FRAME
_ROOM.fields_by_name['processed_videos'].message_type = _PROCESSEDVIDEO
_PROCESSEDVIDEO3D.fields_by_name['frames'].message_type = _FRAME3D
DESCRIPTOR.message_types_by_name['Vector2f'] = _VECTOR2F
DESCRIPTOR.message_types_by_name['Vector3f'] = _VECTOR3F
DESCRIPTOR.message_types_by_name['Pose2D'] = _POSE2D
DESCRIPTOR.message_types_by_name['ReprojectedPose2D'] = _REPROJECTEDPOSE2D
DESCRIPTOR.message_types_by_name['Pose3D'] = _POSE3D
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
DESCRIPTOR.message_types_by_name['Frame3D'] = _FRAME3D
DESCRIPTOR.message_types_by_name['ProcessedVideo'] = _PROCESSEDVIDEO
DESCRIPTOR.message_types_by_name['Room'] = _ROOM
DESCRIPTOR.message_types_by_name['ProcessedVideo3D'] = _PROCESSEDVIDEO3D
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['File'] = _FILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector2f = _reflection.GeneratedProtocolMessageType('Vector2f', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR2F,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Vector2f)
  ))
_sym_db.RegisterMessage(Vector2f)

Vector3f = _reflection.GeneratedProtocolMessageType('Vector3f', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3F,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Vector3f)
  ))
_sym_db.RegisterMessage(Vector3f)

Pose2D = _reflection.GeneratedProtocolMessageType('Pose2D', (_message.Message,), dict(

  Keypoint2D = _reflection.GeneratedProtocolMessageType('Keypoint2D', (_message.Message,), dict(
    DESCRIPTOR = _POSE2D_KEYPOINT2D,
    __module__ = 'suppose_pb2'
    # @@protoc_insertion_point(class_scope:suppose.Pose2D.Keypoint2D)
    ))
  ,
  DESCRIPTOR = _POSE2D,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Pose2D)
  ))
_sym_db.RegisterMessage(Pose2D)
_sym_db.RegisterMessage(Pose2D.Keypoint2D)

ReprojectedPose2D = _reflection.GeneratedProtocolMessageType('ReprojectedPose2D', (_message.Message,), dict(

  ReprojectedKeypoint2D = _reflection.GeneratedProtocolMessageType('ReprojectedKeypoint2D', (_message.Message,), dict(
    DESCRIPTOR = _REPROJECTEDPOSE2D_REPROJECTEDKEYPOINT2D,
    __module__ = 'suppose_pb2'
    # @@protoc_insertion_point(class_scope:suppose.ReprojectedPose2D.ReprojectedKeypoint2D)
    ))
  ,
  DESCRIPTOR = _REPROJECTEDPOSE2D,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.ReprojectedPose2D)
  ))
_sym_db.RegisterMessage(ReprojectedPose2D)
_sym_db.RegisterMessage(ReprojectedPose2D.ReprojectedKeypoint2D)

Pose3D = _reflection.GeneratedProtocolMessageType('Pose3D', (_message.Message,), dict(

  Keypoint3D = _reflection.GeneratedProtocolMessageType('Keypoint3D', (_message.Message,), dict(
    DESCRIPTOR = _POSE3D_KEYPOINT3D,
    __module__ = 'suppose_pb2'
    # @@protoc_insertion_point(class_scope:suppose.Pose3D.Keypoint3D)
    ))
  ,
  DESCRIPTOR = _POSE3D,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Pose3D)
  ))
_sym_db.RegisterMessage(Pose3D)
_sym_db.RegisterMessage(Pose3D.Keypoint3D)

Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), dict(
  DESCRIPTOR = _FRAME,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Frame)
  ))
_sym_db.RegisterMessage(Frame)

Frame3D = _reflection.GeneratedProtocolMessageType('Frame3D', (_message.Message,), dict(
  DESCRIPTOR = _FRAME3D,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Frame3D)
  ))
_sym_db.RegisterMessage(Frame3D)

ProcessedVideo = _reflection.GeneratedProtocolMessageType('ProcessedVideo', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSEDVIDEO,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.ProcessedVideo)
  ))
_sym_db.RegisterMessage(ProcessedVideo)

Room = _reflection.GeneratedProtocolMessageType('Room', (_message.Message,), dict(
  DESCRIPTOR = _ROOM,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Room)
  ))
_sym_db.RegisterMessage(Room)

ProcessedVideo3D = _reflection.GeneratedProtocolMessageType('ProcessedVideo3D', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSEDVIDEO3D,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.ProcessedVideo3D)
  ))
_sym_db.RegisterMessage(ProcessedVideo3D)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.Image)
  ))
_sym_db.RegisterMessage(Image)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'suppose_pb2'
  # @@protoc_insertion_point(class_scope:suppose.File)
  ))
_sym_db.RegisterMessage(File)



_POSEEXTRACTOR = _descriptor.ServiceDescriptor(
  name='PoseExtractor',
  full_name='suppose.PoseExtractor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1009,
  serialized_end=1181,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPose',
    full_name='suppose.PoseExtractor.GetPose',
    index=0,
    containing_service=None,
    input_type=_IMAGE,
    output_type=_FRAME,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamPoses',
    full_name='suppose.PoseExtractor.StreamPoses',
    index=1,
    containing_service=None,
    input_type=_IMAGE,
    output_type=_FRAME,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamPosesFromVideo',
    full_name='suppose.PoseExtractor.StreamPosesFromVideo',
    index=2,
    containing_service=None,
    input_type=_FILE,
    output_type=_FRAME,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSEEXTRACTOR)

DESCRIPTOR.services_by_name['PoseExtractor'] = _POSEEXTRACTOR

# @@protoc_insertion_point(module_scope)
