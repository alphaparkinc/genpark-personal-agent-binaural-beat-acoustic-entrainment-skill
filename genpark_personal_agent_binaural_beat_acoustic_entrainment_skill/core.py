# -*- coding: utf-8 -*-
"""Binaural Beat Acoustic Entrainment Scheduler for GenPark Personal Agent."""
import json
from typing import Dict, Any

class BinauralBeatAcousticEntrainmentScheduler:
    @staticmethod
    def synthesize_binaural_carrier_frequencies(target_state: str, base_carrier_hz: float = 216.0) -> Dict[str, Any]:
        beat_map = {
            "deep_sleep_delta": 2.5,
            "meditative_theta": 6.0,
            "relaxed_flow_alpha": 10.0,
            "hyper_focus_gamma": 40.0
        }
        beat_hz = beat_map.get(target_state, 10.0)
        left_hz = round(base_carrier_hz - (beat_hz / 2.0), 2)
        right_hz = round(base_carrier_hz + (beat_hz / 2.0), 2)
        
        return {
            "target_neuro_state": target_state,
            "binaural_beat_frequency_hz": beat_hz,
            "carrier_frequency_hz": base_carrier_hz,
            "left_ear_frequency_hz": left_hz,
            "right_ear_frequency_hz": right_hz,
            "headphone_requirement": "Stereo headphones mandatory (interaural phase difference requires acoustic isolation)."
        }

    @staticmethod
    def generate_acoustic_entrainment_session_plan(desired_state: str, starting_state: str = "alert_beta", session_duration_minutes: int = 45) -> Dict[str, Any]:
        return {
            "session_total_minutes": session_duration_minutes,
            "target_state": desired_state,
            "frequency_ramp_phases": [
                {"phase": "Phase 1 (0-10 min)", "frequency": "14 Hz (Low Beta) Downramp", "purpose": "Dissolve acute stress and settle ocular saccades"},
                {"phase": "Phase 2 (10-35 min)", "frequency": "10 Hz (Alpha Flow) or 40 Hz (Gamma Focus)", "purpose": "Sustained neurocognitive entrainment core window"},
                {"phase": "Phase 3 (35-45 min)", "frequency": "Stabilization plateau", "purpose": "Cognitive consolidation and peaceful emergence"}
            ],
            "audio_overlay": "Pink noise or 432 Hz ambient drone recommended to mask environmental micro-spikes."
        }
