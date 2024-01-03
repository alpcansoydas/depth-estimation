
# Image Depth Estimator

2D image depth estimation API using ZoeDepth

## Usage/Examples

### CLI Usage
```bash
usage: cli.py [-h] input output

Depth estimation using ZoeDepth

positional arguments:
  input       Path to input image
  output      Path to output image

optional arguments:
  -h, --help  show this help message and exit
```
### API Usage
http://127.0.0.1:8041/predict

## Installation

Install depth-estimator with pip

```bash
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`IMAGE_API_KEY`


## Deployment

To deploy this project run

```bash
  docker build -t - depth_estimation .
  docker run -d -p 8041:8041 depth_estimation

```


## License

[MIT](https://choosealicense.com/licenses/mit/)

