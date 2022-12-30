class OpenablePageMixin:
    def open(self):
        self._open(f"{self.url}/{self.path}")
        return self
