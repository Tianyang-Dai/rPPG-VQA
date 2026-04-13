PROMPT = """
Annotator Task: rPPG Video Data Quality Evaluation
Role: You are a Remote Photoplethysmography (rPPG) Training Data Annotator. Your job is to evaluate the quality of facial videos used for rPPG heart rate estimation.
Objective: Assess each video using the noise-based evaluation dimensions below. For each dimension, assign a score based on the provided criteria to determine the video's quality for rPPG analysis. Higher scores indicate lower noise impact (better quality).
Evaluation Dimensions:
1. Head Movement Noise (0–3 points)
  - Evaluate: The presence, type, and severity of head/body motion and its effect on ROI tracking and potential pulse-frequency confounds. Distinguish benign actions (blinking, slight speech) from disruptive motion (rapid nodding/shaking/turning).
  - Score:
    - 0: Severe movement with frequent rapid rotations/translations, pronounced blur, or repeated ROI tracking failures.
    - 1: Moderate movement or periodic motion likely to inject spurious frequencies or intermittently destabilize tracking.
    - 2: Mild motion (brief expressions/speaking) with stable tracking and negligible blur.
    - 3: Negligible motion; subject remains essentially still with no apparent periodic motion confounds.
2. Illumination Noise (0–3 points)
  - Evaluate: Intensity, uniformity, and stability of facial lighting; presence of flicker, exposure clipping, shadows, or drift over time.
  - Score:
    - 0: Severe issues (strong flicker/strobing, under/overexposure with clipping, large brightness swings, heavy shadowing).
    - 1: Moderate nonuniformity or temporal drift; some shadowing or localized saturation but face remains partly usable.
    - 2: Mild variations; mostly uniform and stable lighting without clipping; minor fluctuations only.
    - 3: Consistently uniform, flicker-free lighting; skin well exposed across the recording.
3. Skin-related Noise (0–2 points)
  - Evaluate: Visibility of subtle skin chrominance changes given skin tone and texture; effects of specular highlights, facial hair, makeup, filters, or partial occlusions on usable skin ROI (forehead/cheeks).
  - Score:
    - 0: Poor visibility—very dark or saturated regions, strong glare, heavy makeup/filters/facial hair, or notable occlusions leaving minimal usable skin.
    - 1: Moderate visibility—usable areas exist but exposure/texture is uneven or partially occluded.
    - 2: Excellent visibility—proper exposure on cheeks/forehead with clear, subtle color variations and minimal occlusion.
4. Camera-related Noise (0–2 points)
  - Evaluate: Sensor and encoding quality affecting rPPG (compression artifacts, color jitter, noise in low light, resolution/focus stability, frame-rate stability, rolling shutter).
  - Score:
    - 0: Heavy compression or pronounced artifacts/noise; low effective detail or unstable focus/frame rate that would significantly impair rPPG.
    - 1: Moderate artifacts/noise; adequate detail with occasional autofocus/gain adjustments or minor instability.
    - 2: Minimal artifacts; high-quality, stable capture with sufficient resolution and faithful color.
Requirements: Based on the above dimensions, score the video content, first stating the evaluation reasons for each dimension, then providing the quality assessment score. The final score is the sum of all dimensions, ranging from 0–10 points. Output format is JSON:
{
  "Evaluation Reasons": {
    "Head Movement Noise": "...",
    "Illumination Noise": "...",
    "Skin-related Noise": "...",
    "Camera-related Noise": "..."
  },
  "Scores": {
    "Head Movement Noise": X,
    "Illumination Noise": X,
    "Skin-related Noise": X,
    "Camera-related Noise": X,
    "Final Score": X
  }
}
Note: Higher scores indicate better quality (lower noise impact) for rPPG applications. Videos scoring 6 or higher are generally suitable for accurate heart rate estimation.
Evaluate the following video:
"""