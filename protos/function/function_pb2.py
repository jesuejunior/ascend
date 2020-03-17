# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/function/function.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/function/function.proto',
  package='function',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eprotos/function/function.proto\x12\x08\x66unction\"\xfd\x02\n\x04\x43ode\x12)\n\x08language\x18\x01 \x01(\x0b\x32\x17.function.Code.Language\x12%\n\x06source\x18\x02 \x01(\x0b\x32\x15.function.Code.Source\x1a\xfc\x01\n\x08Language\x12\x30\n\x06python\x18\x01 \x01(\x0b\x32\x1e.function.Code.Language.PythonH\x00\x1a\xb1\x01\n\x06Python\x12\x13\n\x0bpip_package\x18\x01 \x03(\t\x12\x37\n\x02v2\x18\x02 \x01(\x0b\x32).function.Code.Language.Python.Version.V2H\x00\x12\x37\n\x02v3\x18\x03 \x01(\x0b\x32).function.Code.Language.Python.Version.V3H\x00\x1a\x15\n\x07Version\x1a\x04\n\x02V2\x1a\x04\n\x02V3B\t\n\x07versionB\n\n\x08language\x1a$\n\x06Source\x12\x10\n\x06inline\x18\x02 \x01(\tH\x00\x42\x08\n\x06source\":\n\nExecutable\x12\x1e\n\x04\x63ode\x18\x01 \x01(\x0b\x32\x0e.function.CodeH\x00\x42\x0c\n\nexecutableb\x06proto3')
)




_CODE_LANGUAGE_PYTHON_VERSION_V2 = _descriptor.Descriptor(
  name='V2',
  full_name='function.Code.Language.Python.Version.V2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=355,
  serialized_end=359,
)

_CODE_LANGUAGE_PYTHON_VERSION_V3 = _descriptor.Descriptor(
  name='V3',
  full_name='function.Code.Language.Python.Version.V3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=361,
  serialized_end=365,
)

_CODE_LANGUAGE_PYTHON_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='function.Code.Language.Python.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_CODE_LANGUAGE_PYTHON_VERSION_V2, _CODE_LANGUAGE_PYTHON_VERSION_V3, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=365,
)

_CODE_LANGUAGE_PYTHON = _descriptor.Descriptor(
  name='Python',
  full_name='function.Code.Language.Python',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pip_package', full_name='function.Code.Language.Python.pip_package', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v2', full_name='function.Code.Language.Python.v2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v3', full_name='function.Code.Language.Python.v3', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CODE_LANGUAGE_PYTHON_VERSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='version', full_name='function.Code.Language.Python.version',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=199,
  serialized_end=376,
)

_CODE_LANGUAGE = _descriptor.Descriptor(
  name='Language',
  full_name='function.Code.Language',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='python', full_name='function.Code.Language.python', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CODE_LANGUAGE_PYTHON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='language', full_name='function.Code.Language.language',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=136,
  serialized_end=388,
)

_CODE_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='function.Code.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inline', full_name='function.Code.Source.inline', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='source', full_name='function.Code.Source.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=390,
  serialized_end=426,
)

_CODE = _descriptor.Descriptor(
  name='Code',
  full_name='function.Code',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='function.Code.language', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='function.Code.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CODE_LANGUAGE, _CODE_SOURCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=426,
)


_EXECUTABLE = _descriptor.Descriptor(
  name='Executable',
  full_name='function.Executable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='function.Executable.code', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='executable', full_name='function.Executable.executable',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=428,
  serialized_end=486,
)

_CODE_LANGUAGE_PYTHON_VERSION_V2.containing_type = _CODE_LANGUAGE_PYTHON_VERSION
_CODE_LANGUAGE_PYTHON_VERSION_V3.containing_type = _CODE_LANGUAGE_PYTHON_VERSION
_CODE_LANGUAGE_PYTHON_VERSION.containing_type = _CODE_LANGUAGE_PYTHON
_CODE_LANGUAGE_PYTHON.fields_by_name['v2'].message_type = _CODE_LANGUAGE_PYTHON_VERSION_V2
_CODE_LANGUAGE_PYTHON.fields_by_name['v3'].message_type = _CODE_LANGUAGE_PYTHON_VERSION_V3
_CODE_LANGUAGE_PYTHON.containing_type = _CODE_LANGUAGE
_CODE_LANGUAGE_PYTHON.oneofs_by_name['version'].fields.append(
  _CODE_LANGUAGE_PYTHON.fields_by_name['v2'])
_CODE_LANGUAGE_PYTHON.fields_by_name['v2'].containing_oneof = _CODE_LANGUAGE_PYTHON.oneofs_by_name['version']
_CODE_LANGUAGE_PYTHON.oneofs_by_name['version'].fields.append(
  _CODE_LANGUAGE_PYTHON.fields_by_name['v3'])
_CODE_LANGUAGE_PYTHON.fields_by_name['v3'].containing_oneof = _CODE_LANGUAGE_PYTHON.oneofs_by_name['version']
_CODE_LANGUAGE.fields_by_name['python'].message_type = _CODE_LANGUAGE_PYTHON
_CODE_LANGUAGE.containing_type = _CODE
_CODE_LANGUAGE.oneofs_by_name['language'].fields.append(
  _CODE_LANGUAGE.fields_by_name['python'])
_CODE_LANGUAGE.fields_by_name['python'].containing_oneof = _CODE_LANGUAGE.oneofs_by_name['language']
_CODE_SOURCE.containing_type = _CODE
_CODE_SOURCE.oneofs_by_name['source'].fields.append(
  _CODE_SOURCE.fields_by_name['inline'])
_CODE_SOURCE.fields_by_name['inline'].containing_oneof = _CODE_SOURCE.oneofs_by_name['source']
_CODE.fields_by_name['language'].message_type = _CODE_LANGUAGE
_CODE.fields_by_name['source'].message_type = _CODE_SOURCE
_EXECUTABLE.fields_by_name['code'].message_type = _CODE
_EXECUTABLE.oneofs_by_name['executable'].fields.append(
  _EXECUTABLE.fields_by_name['code'])
_EXECUTABLE.fields_by_name['code'].containing_oneof = _EXECUTABLE.oneofs_by_name['executable']
DESCRIPTOR.message_types_by_name['Code'] = _CODE
DESCRIPTOR.message_types_by_name['Executable'] = _EXECUTABLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Code = _reflection.GeneratedProtocolMessageType('Code', (_message.Message,), dict(

  Language = _reflection.GeneratedProtocolMessageType('Language', (_message.Message,), dict(

    Python = _reflection.GeneratedProtocolMessageType('Python', (_message.Message,), dict(

      Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(

        V2 = _reflection.GeneratedProtocolMessageType('V2', (_message.Message,), dict(
          DESCRIPTOR = _CODE_LANGUAGE_PYTHON_VERSION_V2,
          __module__ = 'protos.function.function_pb2'
          # @@protoc_insertion_point(class_scope:function.Code.Language.Python.Version.V2)
          ))
        ,

        V3 = _reflection.GeneratedProtocolMessageType('V3', (_message.Message,), dict(
          DESCRIPTOR = _CODE_LANGUAGE_PYTHON_VERSION_V3,
          __module__ = 'protos.function.function_pb2'
          # @@protoc_insertion_point(class_scope:function.Code.Language.Python.Version.V3)
          ))
        ,
        DESCRIPTOR = _CODE_LANGUAGE_PYTHON_VERSION,
        __module__ = 'protos.function.function_pb2'
        # @@protoc_insertion_point(class_scope:function.Code.Language.Python.Version)
        ))
      ,
      DESCRIPTOR = _CODE_LANGUAGE_PYTHON,
      __module__ = 'protos.function.function_pb2'
      # @@protoc_insertion_point(class_scope:function.Code.Language.Python)
      ))
    ,
    DESCRIPTOR = _CODE_LANGUAGE,
    __module__ = 'protos.function.function_pb2'
    # @@protoc_insertion_point(class_scope:function.Code.Language)
    ))
  ,

  Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), dict(
    DESCRIPTOR = _CODE_SOURCE,
    __module__ = 'protos.function.function_pb2'
    # @@protoc_insertion_point(class_scope:function.Code.Source)
    ))
  ,
  DESCRIPTOR = _CODE,
  __module__ = 'protos.function.function_pb2'
  # @@protoc_insertion_point(class_scope:function.Code)
  ))
_sym_db.RegisterMessage(Code)
_sym_db.RegisterMessage(Code.Language)
_sym_db.RegisterMessage(Code.Language.Python)
_sym_db.RegisterMessage(Code.Language.Python.Version)
_sym_db.RegisterMessage(Code.Language.Python.Version.V2)
_sym_db.RegisterMessage(Code.Language.Python.Version.V3)
_sym_db.RegisterMessage(Code.Source)

Executable = _reflection.GeneratedProtocolMessageType('Executable', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTABLE,
  __module__ = 'protos.function.function_pb2'
  # @@protoc_insertion_point(class_scope:function.Executable)
  ))
_sym_db.RegisterMessage(Executable)


# @@protoc_insertion_point(module_scope)
