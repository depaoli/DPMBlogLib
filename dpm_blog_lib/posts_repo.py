#!/usr/bin/env python

from git import Repo
import shutil


class PostsRepo(object):

    def __init__(self, url, local_dir):
        self._url = url
        self._local_dir = local_dir
        self.reinitialize()

    def reinitialize(self):
        shutil.rmtree(self._local_dir, ignore_errors=True)
        self._posts_repo = Repo.clone_from(
            self._url,
            self._local_dir,
            depth=1)  # Clone just the HEAD (last version)

    def update(self):
        self._posts_repo.remotes.origin.pull()
