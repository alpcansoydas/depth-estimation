import argparse
from predictor import DepthEstimationModel

def main():
    parser = argparse.ArgumentParser(description = 'Depth estimation using ZoeDepth')
    parser.add_argument('input', type=str, help='Path to input image')
    parser.add_argument('output', type=str, help='Path to output image')
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depthmap(args.input, args.output)
    print(result)

if __name__ == '__main__':
    main()