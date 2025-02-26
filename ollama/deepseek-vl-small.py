
from .DeepSeekVLV2 import DeepseekVLV2ForCausalLM
from .deepseek_vl.processors import DeepseekVLV2Processor

model_path = "deepseek-ai/deepseek-vl2-small"
processor = DeepseekVLV2Processor.from_pretrained(model_path)
model = DeepseekVLV2ForCausalLM.from_pretrained(model_path)
