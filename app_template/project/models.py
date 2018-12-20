from django.db import models
from django.urls import reverse
from webapp.apps.core.models import CoreInputs, CoreRun


class {Project}Inputs(CoreInputs):
    """
    Set inputs fields that are specific to this project's application. Most other
    parameters will be covered in the abstract model class, CoreInputs, but
    some parameters may be specific to this project, such as the
    meta_parameters defined in this project's meta_parameters module.
    """

class {Project}Run(CoreRun):
    """
    Set run or outputs fields that are specific to this project's application.
    Additionally, set the name of the table "dimension." This will be used
    for organizing the outputs. For example, if your project displays data
    on baseball pitchers, this would allow you to toggle a set of tables by
    the pitcher who is being analyzed.
    """
    dimension_name = "Name of table dimension goes here"

    inputs = models.OneToOneField({Project}Inputs, on_delete=models.PROTECT,
                                  related_name='outputs')

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('{project}_outputs', kwargs=kwargs)

    def get_absolute_edit_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('edit_{project}_inputs', kwargs=kwargs)

    def get_absolute_download_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('{project}_download', kwargs=kwargs)

    def zip_filename(self):
        return '{project}.zip'