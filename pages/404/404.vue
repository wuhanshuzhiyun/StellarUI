<template>
	<view class="permission_denied">
		<view id="tsparticles"></view>
		<view class="denied__wrapper">
			<h1>404</h1>
			<h3>页面不存在</h3>
			<img id="astronaut" :src="astronaut" />
			<img id="planet" :src="planet" />
			<a href="#" @click="goToHome"><button class="denied__link">返回首页</button></a>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			astronaut: require('@/static/astronaut.svg'),
			planet: require('@/static/planet.svg'),
		};
	},
	methods: {
		goToHome() {
			// #ifdef H5
			uni.redirectTo({
				url: '/pc/index/index',
			});
			// #endif
			// #ifdef MP
			uni.redirectTo({
				url: '/mp/index/index',
			});
			// #endif
		},
	},
};
</script>
<style lang="scss" scoped>
.particle-error,
.permission_denied,
#tsparticles {
	width: 100vw;
	height: 100vh;
	margin: 0px !important;
}

#tsparticles {
	position: fixed !important;
	opacity: 0.23;
}

.permission_denied {
	background: #24344c !important;
}

.permission_denied a {
	text-decoration: none;
}

.denied__wrapper {
	max-width: 390px;
	width: 100%;
	height: 390px;
	display: block;
	margin: 0 auto;
	position: relative;
}

.permission_denied h1 {
	text-align: center;
	color: #fff;
	font-family: 'Dosis', sans-serif;
	font-size: 100px;
	margin-bottom: 0px;
	font-weight: 800;
}

.permission_denied h3 {
	text-align: center;
	color: #fff;
	font-size: 19px;
	line-height: 23px;
	max-width: 330px;
	margin: 0px auto 30px auto;
	font-family: 'Dosis', sans-serif;
	font-weight: 400;
}

.permission_denied h3 span {
	position: relative;
	width: 65px;
	display: inline-block;
}

.permission_denied h3 span:after {
	content: '';
	border-bottom: 3px solid #ffbb39;
	position: absolute;
	left: 0;
	top: 43%;
	width: 100%;
}

.denied__link {
	background: none;
	color: #fff;
	padding: 12px 0px 10px 0px;
	border: 1px solid #fff;
	outline: none;
	border-radius: 7px;
	width: 150px;
	font-size: 15px;
	text-align: center;
	margin: 0 auto;
	vertical-align: middle;
	display: block;
	margin-bottom: 40px;
	margin-top: 25px;
	font-family: 'Dosis', sans-serif;
	font-weight: 400;
}

.denied__link:hover {
	color: #ffbb39;
	border-color: #ffbb39;
	cursor: pointer;
	opacity: 1;
}

.permission_denied .stars {
	animation: sparkle 1.6s infinite ease-in-out alternate;
}

@keyframes sparkle {
	0% {
		opacity: 1;
	}
	100% {
		opacity: 0.3;
	}
}

#astronaut {
	width: 43px;
	position: absolute;
	right: 20px;
	top: 210px;
	animation: spin 4.5s infinite linear;
}

@keyframes spin {
	0% {
		transform: rotateZ(0deg);
	}
	100% {
		transform: rotateZ(360deg);
	}
}

@media (max-width: 600px) {
	.permission_denied h1 {
		font-size: 75px;
	}
	.permission_denied h3 {
		font-size: 16px;
		width: 200px;
		margin: 0 auto;
		line-height: 23px;
	}
	.permission_denied h3 span {
		width: 60px;
	}
	#astronaut {
		width: 35px;
		right: 40px;
		top: 170px;
	}
}

.saturn,
.saturn-2,
.hover {
	animation: hover 2s infinite ease-in-out alternate;
}

@keyframes hover {
	0% {
		transform: translateY(3px);
	}
	100% {
		transform: translateY(-3px);
	}
}
</style>
