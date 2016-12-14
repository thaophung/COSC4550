#!/usr/bin
set -e

./build/tools/caffe test -model examples/mnist/lenet_test_withoutBN.prototxt -weights examples/mnist/lenet_iter_2000.caffemodel -iterations 240 2>&1 | tee test_lenet_10_image.log
