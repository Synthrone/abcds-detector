#!/usr/bin/env python3

###########################################################################
#
#  Copyright 2024 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

"""ABCD Detector - Video ad analysis using Google AI."""

from abcds_detector.configuration import Configuration
from abcds_detector.models import (
    VideoFeatureCategory,
    FeatureEvaluation,
    VideoAssessment,
)
from abcds_detector.evaluation_services import video_evaluation_service


def analyze_video(
    config: Configuration,
    video_uri: str,
    features_category: VideoFeatureCategory,
) -> list[FeatureEvaluation]:
  """Evaluate video features using ABCD framework.

  Args:
    config: Configuration object with all required parameters
    video_uri: URI of video to analyze (GCS or YouTube URL)
    features_category: Category of features to evaluate (LONG_FORM_ABCD or SHORTS)

  Returns:
    List of evaluated features with detection results
  """
  return video_evaluation_service.video_evaluation_service.evaluate_features(
      config=config,
      video_uri=video_uri,
      features_category=features_category,
  )


__all__ = [
    "Configuration",
    "VideoFeatureCategory",
    "FeatureEvaluation",
    "VideoAssessment",
    "analyze_video",
]
