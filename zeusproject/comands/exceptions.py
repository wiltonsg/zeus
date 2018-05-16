class CreateFolderException(Exception):
    """Create Folder Module."""

    pass


class DuplicateModuleException(Exception):
    """Duplicate Module Name."""

    pass


class DuplicateException(Exception):
    """Duplicate Project Name."""

    pass


class RenameFolder(Exception):
    """Exception Rename Folder."""

    pass