# django pipeline default configuration
## http://django-pipeline.readthedocs.org/en/latest/configuration.html

PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'common': {
        'source_filenames': (
            'sass-bootstrap/lib/bootstrap.scss',
            'sass-bootstrap/dist/css/bootstrap-theme.css',
        ),
        'output_filename': 'css/common.css',
        'extra_context': {'media': 'screen,projection'},
    },
    'app': {
        'source_filenames': ('app/app.sass',),
        'output_filename': 'app/app_out.css',
        'variant': 'datauri',
        'extra_context': {'media': 'screen,projection'},
    }
}

PIPELINE_JS = {
    'common': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'sass-bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/common.js',
    }
}

PIPELINE_SASS_ARGUMENTS = '--compass --trace'
PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'