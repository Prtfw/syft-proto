# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/execution/v1/state_tensor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.torch.v1 import tensor_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2
from syft_proto.types.torch.v1 import parameter_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_parameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/execution/v1/state_tensor.proto',
  package='syft_proto.execution.v1',
  syntax='proto3',
  serialized_options=b'\n$org.openmined.syftproto.execution.v1',
  serialized_pb=b'\n*syft_proto/execution/v1/state_tensor.proto\x12\x17syft_proto.execution.v1\x1a&syft_proto/types/torch/v1/tensor.proto\x1a)syft_proto/types/torch/v1/parameter.proto\"\xad\x01\n\x0bStateTensor\x12K\n\x0ctorch_tensor\x18\x01 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorH\x00R\x0btorchTensor\x12G\n\x0btorch_param\x18\x02 \x01(\x0b\x32$.syft_proto.types.torch.v1.ParameterH\x00R\ntorchParamB\x08\n\x06tensorB&\n$org.openmined.syftproto.execution.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_parameter__pb2.DESCRIPTOR,])




_STATETENSOR = _descriptor.Descriptor(
  name='StateTensor',
  full_name='syft_proto.execution.v1.StateTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torch_tensor', full_name='syft_proto.execution.v1.StateTensor.torch_tensor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='torchTensor', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torch_param', full_name='syft_proto.execution.v1.StateTensor.torch_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='torchParam', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='tensor', full_name='syft_proto.execution.v1.StateTensor.tensor',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=155,
  serialized_end=328,
)

_STATETENSOR.fields_by_name['torch_tensor'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2._TORCHTENSOR
_STATETENSOR.fields_by_name['torch_param'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_parameter__pb2._PARAMETER
_STATETENSOR.oneofs_by_name['tensor'].fields.append(
  _STATETENSOR.fields_by_name['torch_tensor'])
_STATETENSOR.fields_by_name['torch_tensor'].containing_oneof = _STATETENSOR.oneofs_by_name['tensor']
_STATETENSOR.oneofs_by_name['tensor'].fields.append(
  _STATETENSOR.fields_by_name['torch_param'])
_STATETENSOR.fields_by_name['torch_param'].containing_oneof = _STATETENSOR.oneofs_by_name['tensor']
DESCRIPTOR.message_types_by_name['StateTensor'] = _STATETENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateTensor = _reflection.GeneratedProtocolMessageType('StateTensor', (_message.Message,), {
  'DESCRIPTOR' : _STATETENSOR,
  '__module__' : 'syft_proto.execution.v1.state_tensor_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.execution.v1.StateTensor)
  })
_sym_db.RegisterMessage(StateTensor)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
