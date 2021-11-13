import os
import pathlib
import shutil
import threading

from codegen.generators.objects import ObjectsGenerator


def entrypoint():
    models_path = pathlib.Path("vkapipymodels")
    codegen_path = pathlib.Path("codegen")

    shutil.rmtree(models_path, ignore_errors=True)
    models_path.mkdir()
    shutil.copytree(
        codegen_path / "templates" / "bases",
        models_path / "bases"
    )

    codegen = [
        ObjectsGenerator.fetch(models_path)
    ]

    codegen_threads = [
        threading.Thread(target=gen.run_codegen)
        for gen in codegen
    ]

    for thread in codegen_threads:
        thread.start()

    for thread in codegen_threads:
        thread.join()
