from trajectory import Trajectory

result_path = "/home/iadc02/bags/viobot_experiments/"
result_folder = "day_out_1"
resdir = result_path + result_folder

rs_pose = result_folder + "rs.txt"
viobot_pose = result_folder + "viobot.txt"

traj = Trajectory(results_dir=resdir, nm_gt=rs_pose, nm_est=viobot_pose)