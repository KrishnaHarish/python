# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2015 BigML
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


""" Testing prediction creation in DEV mode

"""
from world import world, setup_module, teardown_module
import create_source_steps as source_create
import read_source_steps as source_read
import create_dataset_steps as dataset_create
import create_model_steps as model_create
import create_prediction_steps as prediction_create


class TestDevPrediction(object):

    def setup(self):
        """
            Switches to DEV mode for this class methods only
        """
        world.api = world.api_dev_mode
        world.count_resources('init')

    def teardown(self):
        """ 
            Just for completeness
        """
        pass
        
    def test_scenario1(self):
        """
            Scenario: Successfully creating a prediction in DEV mode:
                Given I want to use api in DEV mode
                When I create a data source uploading a "<data>" file
                And I wait until the source is ready less than <time_1> secs
                And the source has DEV True 
                And I create a dataset
                And I wait until the dataset is ready less than <time_2> secs
                And I create a model
                And I wait until the model is ready less than <time_3> secs
                When I create a prediction for "<data_input>"
                Then the prediction for "<objective>" is "<prediction>"

                Examples:
                | data                | time_1  | time_2 | time_3 | data_input    | objective | prediction  |
                | ../data/iris.csv | 10      | 10     | 10     | {"petal width": 0.5} | 000004    | Iris-setosa |

        """
        print self.test_scenario1.__doc__
        examples = [
            ['data/iris.csv', '10', '10', '10', '{"petal width": 0.5}', '000004', 'Iris-setosa']]
        for example in examples:
            print "\nTesting with:\n", example
            source_create.i_upload_a_file(self, example[0])
            source_create.the_source_is_finished(self, example[1])
            source_read.source_has_dev(self, True)
            dataset_create.i_create_a_dataset(self)
            dataset_create.the_dataset_is_finished_in_less_than(self, example[2])
            model_create.i_create_a_model(self)
            model_create.the_model_is_finished_in_less_than(self, example[3])
            prediction_create.i_create_a_prediction(self, example[4])
            prediction_create.the_prediction_is(self, example[5], example[6])
