from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["jinja2"]}

setup(
	name="Keymap",
	version="0.0.1",
	description="Serveur remote de controle de PC",
    options = {"build_exe": build_exe_options},
	executables= [Executable("KeyRemote_v1_pcb.py")]
)