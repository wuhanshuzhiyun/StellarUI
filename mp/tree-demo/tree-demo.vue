<template>
	<view class="page">
		<page-nav :autoBack="true" backColor="#000" titleAlignment="2" title="树形控件"></page-nav>
		<view class="content">
			<view class="description">
				<view class="cmp-name">Tree 树形控件</view>
				<view class="cmp-desc">用于展示多级列表</view>
			</view>
			<view class="demo-item">
				<view class="title">基础使用</view>
				<ste-tree :options="options" @open="onOpen" @close="onClose"></ste-tree>
			</view>
			<view class="demo-item">
				<view class="title">默认展开节点，打开/关闭指定节点</view>
				<ste-tree ref="accordion" :options="options" :openNodes="['1-2-2']"></ste-tree>
				<ste-button @click="openNode" mode="100">打开标题2</ste-button>
				<ste-button @click="closeNode" mode="100">关闭标题2</ste-button>
			</view>
			<view class="demo-item">
				<view class="title">节点搜索</view>
				<ste-input placeholder="请输入标题内容" v-model="searchTitle"></ste-input>
				<ste-tree :options="options" :searchTitle="searchTitle"></ste-tree>
			</view>
			<view class="demo-item">
				<view class="title">非手风琴模式（展开时不关闭兄弟节点）</view>
				<ste-tree :options="options" :accordion="false"></ste-tree>
			</view>
			<view class="demo-item">
				<view class="title">懒加载</view>
				<ste-tree :options="options1" @beforeOpen="beforeOpen"></ste-tree>
			</view>
			<view class="demo-item">
				<view class="title">自定义内容</view>
				<ste-tree :options="options">
					<template v-slot="{ node, depth }">
						<view class="item-title">
							<image
								v-if="depth === 0"
								class="title-image"
								src="https://image.whzb.com/chain/StellarUI/component-icons/ste-tree.png"
							></image>
							<image
								v-if="depth === 1"
								class="title-image"
								src="https://image.whzb.com/chain/StellarUI/component-icons/ste-tree-children.png"
							></image>
							<view class="item-text">{{ node.title }}</view>
						</view>
					</template>
					<template v-slot:open="{ open }">
						<view class="slef-open-icon">
							{{ open ? '-' : '+' }}
						</view>
					</template>
				</ste-tree>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			searchTitle: '',
			options: [
				{
					title: '标题1',
					value: '1',
					children: [
						{
							title: '标题1-1',
							value: '1-1',
							children: [
								{ title: '标题-1-1', value: '1-1-1' },
								{ title: '标题1-1-2', value: '1-1-2' },
							],
						},
						{
							title: '标题1-2',
							value: '1-2',
							children: [
								{ title: '标题1-2-1', value: '1-2-1' },
								{
									title: '标题1-2-2',
									value: '1-2-2',
									children: [{ title: '标题1-2-2-1', value: '1-2-2-1' }],
								},
							],
						},
					],
				},
				{
					title: '标题2',
					value: '2',
					children: [{ title: '标题2-1', value: '2-1' }],
				},
			],
			options1: [
				{ title: '标题1', value: '1', hasChildren: true },
				{ title: '标题2', value: '2', hasChildren: true },
			],
		};
	},
	methods: {
		beforeOpen(node, suspend, next, stop) {
			// 开启等待
			suspend();
			setTimeout(() => {
				// 继续后续操作，并将结果传递给next
				next([
					{ title: `${node.title}-1`, value: `${node.value}-1` },
					{ title: `${node.title}-2`, value: `${node.value}-2`, hasChildren: true },
				]);
			}, 2000);
		},
		onOpen(node) {
			this.$showToast({ title: `打开节点：${node.title}`, icon: 'none' });
		},
		onClose(node) {
			this.$showToast({ title: `关闭节点：${node.title}`, icon: 'none' });
		},
		openNode() {
			this.$refs.accordion.open('2');
		},
		closeNode() {
			this.$refs.accordion.close('2');
		},
		getImage(detph) {
			return this.images[depth];
		},
	},
	mounted() {},
};
</script>

<style lang="scss" scoped>
.page {
	background-color: #f5f5f5;
	.content {
		.item-title {
			width: 100%;
			height: 80rpx;
			line-height: 80rpx;
			display: flex;
			padding-left: 20rpx;
			align-items: center;
			.title-image {
				width: 48rpx;
				height: 48rpx;
				margin-right: 16rpx;
			}
		}
	}
}
</style>
