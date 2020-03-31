from distutils.core import setup, Extension

setup(
    name="murmur2",
    version="1.0.2",
    ext_modules=[
        Extension(
            "murmur2",
            [
                "src/murmur2.cc",
                "src/MurmurHash2.cpp",
            ],
            include_dirs=[
                "include/"
            ],

        )
    ],
    url="https://github.com/orion46/murmur2",
    author="Nobutaka Ito",
    author_email="earth.nobu.light@gmail.com",
    description="murmur2_64a python wrapper"
)
