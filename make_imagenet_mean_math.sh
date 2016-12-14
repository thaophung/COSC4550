#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/imagenet
DATA=data/math/
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/math_train_first_lmdb \
	$EXAMPLE/math_first_mean.binaryproto

echo "Done."
