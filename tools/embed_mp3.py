import pathlib
import sys


source = pathlib.Path(sys.argv[1])
destination = pathlib.Path(sys.argv[2])
data = source.read_bytes()

values = ",\n".join(
    "    " + ", ".join(f"0x{byte:02x}" for byte in data[index:index + 16])
    for index in range(0, len(data), 16)
)

destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(
    "#ifndef SLOW_MP3_H\n"
    "#define SLOW_MP3_H\n\n"
    "#include <stddef.h>\n"
    "#include <stdint.h>\n\n"
    "static const uint8_t slow_mp3_data[] = {\n"
    f"{values}\n"
    "};\n\n"
    "static const size_t slow_mp3_size = sizeof(slow_mp3_data);\n\n"
    "#endif\n",
    encoding="ascii",
)