# django pipeline default configuration
## http://django-pipeline.readthedocs.org/en/latest/configuration.html

# PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'app': {
        'source_filenames': (
            'lightbox/dist/ekko-lightbox.css',
            'app/css/app.css',
        ),
        'output_filename': 'common.css',
        'extra_context': {'media': 'screen,projection'},
    }
}

PIPELINE_JS = {
    'common': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'bootstrap-sass-3.3.2/assets/javascripts/bootstrap.js',
            'lightbox/dist/ekko-lightbox.js',
            'wysihtml-0.4.17/dist/wysihtml5x-toolbar.min.js',
            'wysihtml-0.4.17/parser_rules/advanced_and_extended.js',
            'app/app.js',
        ),
        'output_filename': 'js/common.js',
    }
}


# PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

# MANIFESTO_EXCLUDED_MANIFESTS = (
        # 'randomapp.manifest.WrongManifest',
# )
