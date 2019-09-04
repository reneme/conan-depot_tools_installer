#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class DepotToolsConan(ConanFile):
    name = "depot_tools_installer"
    version = "master"
    license = "Chromium"
    description = "A collection of tools for dealing with Chromium development"
    url = "https://github.com/SSE4/conan-depot_tools_installer"
    no_copy_source = True
    short_paths = True
    settings = {"os"}
    repository = "https://chromium.googlesource.com/chromium/tools/depot_tools.git"

    checkout_folder = "depot_tools"

    def source(self):
        git = tools.Git(folder=self.checkout_folder)
        git.clone(self.repository)

    def package(self):
        self.copy(pattern="*", dst=".", src=self.checkout_folder)

    def package_info(self):
        self.env_info.PATH.append(self.package_folder)
