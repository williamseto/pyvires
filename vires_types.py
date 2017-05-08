# import socket
# import time
# import numpy as np
# import struct, collections

from ctypes import *

RDB_MAGIC_NO = 35712
RDB_PKG_ID_START_OF_FRAME = 1
class RDB_MSG_HDR_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('magicNo', c_ushort),
        ('version', c_ushort),
        ('headerSize', c_uint),
        ('dataSize', c_uint),
        ('frameNo', c_uint),
        ('simTime', c_double)]

class RDB_MSG_ENTRY_HDR_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('headerSize', c_uint),
        ('dataSize', c_uint),
        ('elementSize', c_uint),
        ('pkgId', c_ushort),
        ('flags', c_ushort)]

class RDB_GEOMETRY_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('dimX', c_float),
        ('dimY', c_float),
        ('dimZ', c_float),
        ('offX', c_float),
        ('offY', c_float),
        ('offZ', c_float)]

class RDB_COORD_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('x', c_double),
        ('y', c_double),
        ('z', c_double),
        ('h', c_float),
        ('p', c_float),
        ('r', c_float),
        ('flags', c_ubyte),
        ('type', c_ubyte),
        ('system', c_ushort)]

class RDB_OBJECT_STATE_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('id', c_uint),
        ('category', c_ubyte),
        ('type', c_ubyte),
        ('visMask', c_ushort),
        ('name', c_char*32),
        ('geo', RDB_GEOMETRY_t),
        ('pos', RDB_COORD_t),
        ('parent', c_uint),
        ('cfgFlags', c_ushort),
        ('cfgModelId', c_short)]

class RDB_SENSOR_STATE_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('id', c_uint),
        ('type', c_ubyte),
        ('hostCategory', c_ubyte),
        ('spare0', c_ushort),
        ('hostId', c_uint),
        ('name', c_char*32),
        ('fovHV', c_float*2),
        ('clipNF', c_float*2),
        ('pos', RDB_COORD_t),
        ('originCoordSys', RDB_COORD_t),
        ('fovOffHV', c_float*2),
        ('spare', c_int*4)]

class RDB_SENSOR_OBJECT_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('category', c_ubyte),
        ('type', c_ubyte),
        ('flags', c_ushort),
        ('id', c_uint),
        ('sensorId', c_uint),
        ('dist', c_double),
        ('sensorPos', RDB_COORD_t),
        ('occlusion', c_byte),
        ('spare0', c_ubyte*3),
        ('spare', c_int*3)]

SCP_MAGIC_NO = 40108

class SCP_MSG_HDR_t(Structure):
    _pack_ = 4
    _fields_ = [
        ('magicNo', c_ushort),
        ('version', c_ushort),
        ('sender', c_char*64),
        ('receiver', c_char*64),
        ('dataSize', c_uint)]