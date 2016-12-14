#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs

EXAMPLE=examples/imagenet
DATA=data/math/
TOOLS=build/tools

TEST_DATA_ROOT=data/math/

# Set RESIZE=true to resize the images to 256x256. Leave as false
# if images have already been resized using another tool

#RESIZE=false
#if $RESIZE; then
#        RESIZE_HEIGHT=256
#        RESIZE_WIDTH=256
#else
#        RESIZE_HEIGHT=0
#        RESIZE_WIDTH=0
#fi

        echo "Set the TEST_DATA_ROOT variable in create_imagenet.sh to the path" \
                " where the ImageNet training data is stored."
        exit 1
fi

echo "Creating test lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
        --resize_height=$RESIZE_HEIGHT \
        --resize_width=$RESIZE_WIDTH \
        --shuffle \
        $TEST_DATA_ROOT \
        $DATA/test.txt \
        $EXAMPLE/math_test_lmdb
echo "Done"
