<template>
	<view class="page">
		<page-nav :autoBack="true" backColor="#000" titleAlignment="2" title="轮播组件"></page-nav>
		<view class="content">
			<view class="description">
				<view class="cmp-name">Swiper 轮播组件</view>
				<view class="cmp-desc">用于循环轮播一组图片或内容，也可以滑动进行切换，轮播动效时间可以设置。</view>
			</view>
			<view class="type-block">
				<view>01 组件类型</view>
			</view>
			<view class="demo-item">
				<view class="title">基础用法（必须固定宽度，默认100%）</view>
				<view class="item-view">
					<ste-swiper>
						<ste-swiper-item v-for="(m, index) in list1" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">纵向轮播（必须固定高度，默认100%）</view>
				<view class="item-view">
					<ste-swiper direction="vertical" height="300rpx">
						<ste-swiper-item v-for="(m, index) in list1" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">首尾衔接轮播</view>
				<view class="item-view">
					<ste-swiper circular>
						<ste-swiper-item v-for="(m, index) in list1" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">自动轮播</view>
				<view class="item-view">
					<ste-swiper circular autoplay @change="onChange">
						<ste-swiper-item v-for="(m, index) in list1" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
			<view class="type-block">
				<view>02 组件样式</view>
			</view>
			<view class="demo-item">
				<view class="title">显示指示器</view>
				<view class="item-view">
					<ste-swiper circular autoplay indicatorDots>
						<ste-swiper-item v-for="(m, index) in list2" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">指示器颜色</view>
				<view class="item-view">
					<ste-swiper circular autoplay indicatorDots indicatorColor="#0f0" indicatorActiveColor="#f00">
						<ste-swiper-item v-for="(m, index) in list2" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
			<view class="demo-item">
				<view class="title">显示前后页</view>
				<view class="item-view">
					<ste-swiper circular autoplay previousMargin="60" nextMargin="60">
						<ste-swiper-item v-for="(m, index) in list2" :index="index" :key="index">
							<image :src="m" class="item" />
						</ste-swiper-item>
					</ste-swiper>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			list1: [
				'https://image.whzb.com/chain/StellarUI/image/banner1.png',
				'https://image.whzb.com/chain/StellarUI/image/banner2.png',
			],
			list2: [
				'https://image.whzb.com/chain/StellarUI/image/banner1.png',
				'https://image.whzb.com/chain/StellarUI/image/banner2.png',
				'https://image.whzb.com/chain/StellarUI/image/banner1.png',
				'https://image.whzb.com/chain/StellarUI/image/banner2.png',
			],
		};
	},
	methods: {
		onChange(index, source) {
			console.log(index, source);
		},
	},
};
</script>
<style lang="scss" scoped>
.page {
	.content {
		.item {
			height: 300rpx;
		}
	}
}
</style>
