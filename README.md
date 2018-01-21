find_sequence_frame_range is a script to finds all animated sequences in a given directory. 
And prints their frame ranges in the following format: 

  - 'name: 1001-2000' -if there are no gaps
  - 'name: 1001, 1003-1500, 1600-2000' - if there are gaps
  
The format for an animated sequence is name.####.ext 
   - e.g. /job/.../my_render_v001.1001.jpg



**Usage**
```python
>>> get_sequence_frame_range_on_disk(file_dir='C:\tmp')
{'flower': ['0000-0005', '0007', '0009'], 'dog': ['0000'], 'cat': ['0000']}

```
