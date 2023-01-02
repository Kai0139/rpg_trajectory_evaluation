#!/usr/bin/env python3

# import rosbag
import os
import argparse
import baggie

def to_sec(ts):
    return ts.sec + ts.nanosec/1e9

def extract(bagfile, pose_topic, msg_type, out_filename):
    n = 0
    f = open(out_filename, 'w')
    f.write('# timestamp tx ty tz qx qy qz qw\n')
    with baggie.BagReader(bagfile) as bag:
        for topic, msg, ts in bag.read_messages():
            if msg_type == "Odometry" and topic == pose_topic:
                f.write('%.12f %.12f %.12f %.12f %.12f %.12f %.12f %.12f\n' %
                        (to_sec(msg.header.stamp),
                         msg.pose.pose.position.x, msg.pose.pose.position.y,
                         msg.pose.pose.position.z,
                         msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
                         msg.pose.pose.orientation.z, msg.pose.pose.orientation.w))
            n += 1
    print('wrote ' + str(n) + ' imu messages to the file: ' + out_filename)


if __name__ == '__main__':
    cmd_ln = False
    if cmd_ln:
        parser = argparse.ArgumentParser(description='''
        Extracts IMU messages from bagfile.
        ''')
        parser.add_argument('bag', help='Bagfile')
        parser.add_argument('topic', help='Topic')
        parser.add_argument('--msg_type', default='PoseStamped',
                            help='message type')
        parser.add_argument('--output', default='stamped_poses.txt',
                            help='output filename')
        args = parser.parse_args()

        out_dir = os.path.dirname(os.path.abspath(args.bag))
        out_fn = os.path.join(out_dir, args.output)

        print('Extract pose from bag '+args.bag+' in topic ' + args.topic)
        print('Saving to file '+out_fn)
        extract(args.bag, args.topic, args.msg_type, out_fn)
    else:
        home_dir = os.environ["HOME"]
        bag_dir = home_dir + "/rosbags/viobot_experiments/rs_bags/" + "night1.bag"
        topic = "/camera/pose/sample"
        msg_type = "Odometry"
        out_fn = home_dir + "/rosbags/viobot_experiments/rs_bags/" + "night1.txt"
        extract(bag_dir, topic, msg_type, out_fn)

