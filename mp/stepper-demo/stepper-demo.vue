<template>
	<view class="page">
		<page-nav :autoBack="true" backColor="#000" titleAlignment="2" title="步进器"></page-nav>
		<view class="content">
			<view class="description">
				<view class="cmp-name">Stepper 步进器</view>
				<view class="cmp-desc">
					用户通过调整“+”按钮、“-”按钮、数字输入框来调整具体需要的数值，可设置最大值和最小值
				</view>
			</view>
			<view class="demo-item">
				<view class="title">基础用法</view>
				<view class="item-block">
					<ste-stepper v-model="value1"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">限制输入范围</view>
				<view class="item-block">
					<ste-stepper v-model="value2" :min="5" :max="15"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">步长设置</view>
				<view class="item-block">
					<ste-stepper v-model="value3" :step="2"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">数值精度</view>
				<view class="item-block">
					<ste-stepper v-model="value4" :precision="1"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">自定义大小</view>
				<view class="item-block">
					<ste-stepper v-model="value5" inputWidth="100" btnSize="70"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">设置主色</view>
				<view class="item-block">
					<ste-stepper v-model="value6" mainColor="#f73131"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">禁用状态</view>
				<view class="item-block stepper-box">
					<div class="box">
						<div>
							<ste-stepper v-model="value7" disabled></ste-stepper>
							<ste-text class="text">禁用步进器</ste-text>
						</div>
						<div>
							<ste-stepper v-model="value8" disablePlus></ste-stepper>
							<ste-text class="text">禁用增加按钮</ste-text>
						</div>
					</div>
					<div class="box">
						<div>
							<ste-stepper v-model="value10" disableInput></ste-stepper>
							<ste-text class="text">禁用输入框</ste-text>
						</div>
						<div>
							<ste-stepper v-model="value9" disableMinus></ste-stepper>
							<ste-text class="text">禁用减少按钮</ste-text>
						</div>
					</div>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">样式风格：线性风格</view>
				<view class="item-block stepper-box">
					<ste-stepper v-model="value11" theme="line"></ste-stepper>
					<div class="box">
						<div>
							<ste-stepper v-model="value12" theme="line" disabled></ste-stepper>
							<ste-text class="text">禁用步进器</ste-text>
						</div>
						<div>
							<ste-stepper v-model="value13" theme="line" disablePlus></ste-stepper>
							<ste-text class="text">禁用增加按钮</ste-text>
						</div>
					</div>
					<div class="box">
						<div>
							<ste-stepper v-model="value14" theme="line" disableInput></ste-stepper>
							<ste-text class="text">禁用输入框</ste-text>
						</div>
						<div>
							<ste-stepper v-model="value15" theme="line" disableMinus></ste-stepper>
							<ste-text class="text">禁用减少按钮</ste-text>
						</div>
					</div>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">样式风格：纯加购按钮</view>
				<view class="item-block">
					<ste-stepper v-model="value16" theme="add"></ste-stepper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">回调事件</view>
				<view class="item-block stepper-box">
					<ste-stepper v-model="value17" @blur="blur" @focus="focus"></ste-stepper>
					<ste-text>失焦事件和聚焦事件</ste-text>
					<ste-stepper v-model="value18" @plus="click1" @minus="click1" @change="change"></ste-stepper>
					<text>在plus或minus事件后，执行change事件</text>
					<ste-stepper v-model="value19" @plus="click2" @minus="click2" @change="change"></ste-stepper>
					<text>在plus或minus事件后，阻止change事件</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			value1: 10,
			value2: 7,
			value3: 2,
			value4: 5.8,
			value5: 5,
			value6: 6,
			value7: 7,
			value8: 8,
			value9: 9,
			value10: 10,
			value11: 11,
			value12: 12,
			value13: 13,
			value14: 14,
			value15: 15,
			value16: 16,
			value17: 17,
			value18: 18,
			value19: 19,
		};
	},
	methods: {
		blur(event) {
			this.$showToast({
				icon: 'none',
				title: `失焦事件`,
			});
		},
		focus() {
			this.$showToast({
				icon: 'none',
				title: `聚焦事件`,
			});
		},
		click1(value) {
			this.$showToast({
				icon: 'none',
				title: `点击按钮：${value} 输入值`,
			});
		},
		click2(value, allowStop, resolve) {
			this.$showToast({
				icon: 'none',
				title: `点击按钮：${value} 输入值`,
			});
			// 阻止change事件
			allowStop();
		},
		change(value) {
			setTimeout(() => {
				this.$showToast({
					icon: 'none',
					title: `改变：${value} 输入值`,
				});
			}, 1000);
		},
	},
};
</script>

<style lang="scss" scoped>
.page {
	.stepper-box {
		flex-direction: column !important;
		row-gap: 20rpx;
		align-items: flex-start !important;
		justify-content: center;

		.box {
			display: flex;
			column-gap: 40rpx;
		}

		.text {
			font-size: 20rpx;
		}
	}
}
</style>
