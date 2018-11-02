"""
This file may be in part a direct translation of the original Cube 2 sources into python.
Please see readme_source.txt for the license that may apply.
"""
from sour.common.ivec import C, R, ivec
from sour.map.facevec import facevec
from sour.map.dimension import dimension, dimcoord, octacoord
from sour.common.constants import empty_material_types, material_types, F_SOLID
from sour.map.Cube import touchingface, notouchingface
from sour.map.insideface import insideface
from sour.map.faceedges import faceedges
from sour.map.genfacevecs import genfacevecs
from sour.map.clipfacevecs import clipfacevecs
from sour.map.isliquid import isliquid
from sour.map.isclipped import isclipped


def occludesface(c, orient, o, size, vo, vsize, vmat, nmat, matmask, vf, numv):
    dim = dimension(orient)

    if c.children == 0:
        if nmat != empty_material_types.MAT_AIR and (c.material & matmask) == nmat:
            nf = [facevec() for _ in xrange(8)]
            return clipfacevecs(vf, numv, o[C[dim]], o[R[dim]], size, nf) < 3

        if c.isentirelysolid():
            return True

        if vmat != empty_material_types.MAT_AIR and (
            (c.material & matmask) == vmat
            or (isliquid(vmat) and isclipped(c.material & material_types.MATF_VOLUME))
        ):
            return True

        if touchingface(c, orient) and faceedges(c, orient) == F_SOLID:
            return True

        cf = [facevec() for _ in xrange(8)]
        numc = clipfacevecs(vf, numv, o[C[dim]], o[R[dim]], size, cf)

        if numc < 3:
            return True

        if c.isempty() or notouchingface(c, orient):
            return False

        of = [facevec() for _ in xrange(4)]

        numo = genfacevecs(c, orient, o, size, False, of)

        return numo >= 3 and insideface(cf, numc, of, numo)

    size >>= 1
    coord = dimcoord(orient)

    for i in xrange(8):
        if octacoord(dim, i) == coord:
            if (
                occludesface(
                    c.children[i],
                    orient,
                    ivec(i, o.x, o.y, o.z, size),
                    size,
                    vo,
                    vsize,
                    vmat,
                    nmat,
                    matmask,
                    vf,
                    numv,
                )
                == 0
            ):
                return False

    return True
