
## 主要内容

- `Energy_management_controller.slx`：自定义能量管理控制器
- `Brain.m`：Simulink 与 Python 网络推理的接口
- `Network.py`：TensorFlow 1.x 兼容模式下的网络推理
- `MODEL/`：TensorFlow 检查点
- `StrategyData/`：策略输入/输出数据
- `Current_velocity.*`、`Powerforfilter.*`、`WLTC.xlsx`：仿真数据

## 运行条件

- MATLAB/Simulink（原说明指定 MATLAB 2014a）
- 合法安装的 ADVISOR 2002
- Python、NumPy、TensorFlow（代码使用 `tensorflow.compat.v1`）

原工程中的 `*.mexw64` 编译二进制、`slprj/` 构建缓存和完整 `advisor/` 第三方目录未纳入版本库。若模型依赖这些二进制，需要在本地从对应源代码重新构建或从原工程受控恢复。

## 许可

当前未附加开源许可证。在版权所有者明确授权之前，请勿假定本仓库内容可被复制、修改或再分发。ADVISOR 自身的许可不由本仓库授予。
