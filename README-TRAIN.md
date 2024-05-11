```shell
mkdir data_root/main
python preprocess.py --data_root data_root/main --preprocessed_root data_root/lrs2_preprocessed/ --batch_size 4
python preprocess.py --data_root data_root/test --preprocessed_root data_root/lrs2_preprocessed1/ --batch_size 4
python train_syncnet_sam.py
python hq_wav2lip_sam_train.py --checkpoint_path checkpoints/wav/gen_checkpoint_384_2_000084000_2024-05-09.pth --syncnet_checkpoint_path checkpoints/syncnet/actor/best_syncnet_actor.pth
```