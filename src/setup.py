from setuptools import setup

setup(name='lipnet',
    version='0.1.6',
    description='End-to-end sentence-level lipreading',
    packages=['lipnet'],
    zip_safe=False,
	install_requires=[
        'Keras==2.0.2',
        'editdistance==0.3.1',
		'h5py==2.10.0',
		'matplotlib==2.2.5',
		'numpy==1.19.1',
		'python-dateutil==2.8.0',
		'scipy==1.2.3',
		'Pillow==4.3.0',
		'tensorflow==1.13.1',
		'Theano==0.9.0',
        'nltk==3.2.2',
        'sk-video==1.1.10',
        'dlib'
    ])