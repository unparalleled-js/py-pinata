from pathlib import Path

from pynata.clients.base import PinataClient
from pynata.response import PinataResponse


class PinningClient(PinataClient):
    def pin_file(self, file_path: Path) -> PinataResponse:
        """
        Add and pin any file, or directory, to Pinata's IPFS nodes.

        Args:
            file_path (pathlib.Path): The path to the file to pin.

        Returns:
            :class:`~pynata.response.PinataResponse`
        """
        paths = [f for f in file_path.iterdir()] if file_path.is_dir() else [file_path]
        files = (
            [("file", (str(path), open(path, "rb"))) for path in paths]
            if file_path.is_dir()
            else [("file", open(path, "rb")) for path in paths]
        )
        return self.session.post("pinning/pinFileToIPFS", files=files)

    def pin_json(self, json_file_path: Path) -> PinataResponse:
        """
        Add and pin any JSON object they wish to Pinata's IPFS nodes. This endpoint is
        specifically optimized to only handle JSON content.

        Args:
            json_file_path (pathlib.Path): The path to a JSON file.

        Returns:
            :class:`~pynata.response.PinataResponse`
        """
        raise NotImplemented("TODO")

    def pin_hash(self, hash_: str) -> PinataResponse:
        """
        Add a hash to Pinata for asynchronous pinning. Content added through this endpoint
        is pinned in the background and will show up in your pinned items once the content
        has been found/pinned. **For this operation to succeed, the content for the hash you
        provide must already be pinned by another node on the IPFS network.**

        Args:
            hash_: The hash to pin.

        Returns:
            :class:`~pynata.response.PinataResponse`
        """
        raise NotImplemented("TODO")

    def unpin(self, content_hash: str) -> PinataResponse:
        """
        Unpin content they previously uploaded to Pinata's IPFS nodes.

        Args:
            content_hash (str): The hash of the content to stop pinning.

        Returns:
            :class:`~pynata.response.PinataResponse`
        """
        url = f"/pinning/unpin/{content_hash}"
        return self.session.delete(url)


__all__ = ["PinningClient"]
