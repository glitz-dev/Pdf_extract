#!/usr/bin/env python3
"""
Test script to verify cache directory setup and T5 model loading
"""

import os
import sys

def test_cache_directories():
    """Test that cache directories are properly set up"""
    print("Testing cache directory setup...")
    
    # Test cache directories
    cache_dirs = [
        '/app/.cache/huggingface',
        '/app/.cache/torch',
        '/root/.cache/huggingface',
        '/root/.cache/torch'
    ]
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            print(f"✓ {cache_dir} exists")
            # Check if writable
            if os.access(cache_dir, os.W_OK):
                print(f"✓ {cache_dir} is writable")
            else:
                print(f"✗ {cache_dir} is not writable")
        else:
            print(f"✗ {cache_dir} does not exist")
    
    # Test environment variables
    env_vars = ['HF_HOME', 'TRANSFORMERS_CACHE', 'TORCH_HOME']
    for var in env_vars:
        if var in os.environ:
            print(f"✓ {var} = {os.environ[var]}")
        else:
            print(f"✗ {var} not set")

def test_t5_loading():
    """Test T5 model loading with cache directory"""
    print("\nTesting T5 model loading...")
    
    try:
        from transformers import T5Tokenizer, T5ForConditionalGeneration
        import torch
        
        print("✓ Transformers imported successfully")
        
        # Test with explicit cache directory
        cache_dir = '/app/.cache/huggingface'
        model_name = "t5-small"
        
        print(f"Loading {model_name} with cache_dir={cache_dir}...")
        
        tokenizer = T5Tokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        print("✓ Tokenizer loaded successfully")
        
        model = T5ForConditionalGeneration.from_pretrained(model_name, cache_dir=cache_dir)
        print("✓ Model loaded successfully")
        
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model.to(device)
        print(f"✓ Model moved to {device}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error loading T5 model: {e}")
        return False

if __name__ == "__main__":
    print("Cache Directory and T5 Model Test")
    print("=" * 40)
    
    test_cache_directories()
    
    if test_t5_loading():
        print("\n✓ All tests passed! Cache directory fix is working.")
    else:
        print("\n✗ Some tests failed. Check the error messages above.")
        sys.exit(1)
