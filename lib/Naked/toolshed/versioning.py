#!/usr/bin/env python
# encoding: utf-8

#TODO : add to tests

class VersionEditor:
    def __init__(self, major_version, minor_version, patch_version):
        self.major_version = major_version
        self.minor_version = minor_version
        self.patch_version = patch_version

    # increment patch version by 1
    def increment_version_patch(self):
        patch_int = int(self.patch_version) # convert to int
        patch_int += 1
        return str(patch_int) # return as a string

    # increment the minor version by 1
    def increment_version_minor(self):
        minor_int = int(self.minor_version)
        minor_int += 1
        return str(minor_int)

    # increment the major version by 1
    def increment_version_major(self):
        major_int = int(self.major_version)
        major_int += 1
        return str(major_int)

if __name__ == '__main__':
    pass
