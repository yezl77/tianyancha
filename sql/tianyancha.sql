CREATE TABLE t_company (
	id VARCHAR ( 100 ) NOT NULL comment "公司id url",
	img VARCHAR ( 100 )  comment "log图片",
	compCh VARCHAR ( 300 ) comment "公司全称",
	compEn VARCHAR ( 300 ) comment "英文名称",
	sscym VARCHAR ( 300 ) comment "上市曾用名",
	gsdj VARCHAR ( 300 ) comment "工商登记",
	zczb VARCHAR ( 300 ) comment "注册资本",
	sshy VARCHAR ( 300 ) comment "所属行业",
	dsz VARCHAR ( 300 ) comment "董事长",
	dm VARCHAR ( 300 ) comment "董秘",
	fddbr VARCHAR ( 300 ) comment "法定代表人",
	zjl VARCHAR ( 300 ) comment "总经理",
	ygrs VARCHAR ( 300 ) comment "员工人数",
	glryrs VARCHAR ( 300 ) comment "管理人员人数",
	kggd VARCHAR ( 300 ) comment "控股股东",
	sjkzr VARCHAR ( 300 ) comment "实际控制人",
	zzkzr VARCHAR ( 300 ) comment "最终控制人",
	zyyw VARCHAR ( 2000 ) comment "主营业务",
	agdm VARCHAR ( 300 ) comment "A股代码",
	agjc VARCHAR ( 300 ) comment "A股简称",
	bgdm VARCHAR ( 300 ) comment "B股代码",
	bgjc VARCHAR ( 300 ) comment "B股简称",
	hgdm VARCHAR ( 300 ) comment "H股代码",
	hgjc VARCHAR ( 300 ) comment "H股简称",
	zqlb VARCHAR ( 300 ) comment "证券类别",
	lxdh VARCHAR ( 300 ) comment "联系电话",
	dzyx VARCHAR ( 300 ) comment "电子邮箱",
	cz VARCHAR ( 300 ) comment "传真",
	gswz VARCHAR ( 300 ) comment "公司网址",
	qy VARCHAR ( 300 ) comment "区域",
	yzbm VARCHAR ( 300 ) comment "邮政编码",
	bgdz VARCHAR ( 300 ) comment "办公地址",
	zcdz VARCHAR ( 300 ) comment "注册地址",
	fddbrr VARCHAR (100) comment "法定代表人",
	zczb1 varchar(300) comment "注册资本",
	sjzb1 varchar(300) comment "实缴资本",
	clrq1 varchar(300) comment "成立日期",
	jyzt1 varchar(300) comment "经营状态",
	tyshxxdm1 varchar(300) comment "统一社会信用代码",
	gszc1 varchar(300) comment "工商注册号",
	nsrsbh1 varchar(300) comment "纳税人识别号",
	zzjgdm1 varchar(300) comment "组织机构代码",
	gslx1 varchar(300) comment "公司类型",
	hy1 varchar(300) comment "行业",
	hzrq1 varchar(300) comment "核准日期",
	djjg1 varchar(300) comment "登记机关",
	yyqx1 varchar(300) comment "营业期限",
	nsrzz1 varchar(300) comment "纳税人资质",
	rygm1 varchar(300) comment "人员规模",
	cbrs1 varchar(300) comment "参保人数",
	cym1 varchar(300) comment "曾用名",
	ywmc1 varchar(300) comment "英文名称",
	zcdz1 varchar(300) comment "注册地址",
	jyfw1 varchar(2000) comment "经营范围",
	flag  tinyint(1)  comment "是否查找完毕",
    PRIMARY KEY ( id )
)

CREATE TABLE `t_industry`  (
  `industry` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '行业',
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '行业url',
  `flag` tinyint(1) NULL DEFAULT NULL COMMENT '是否完成'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


CREATE TABLE `t_industry_province`  (
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分页链接',
  `flag` tinyint(1) NULL DEFAULT NULL COMMENT '是否爬过',
  PRIMARY KEY (`href`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for t_industry_province_city
-- ----------------------------
DROP TABLE IF EXISTS `t_industry_province_city`;
CREATE TABLE `t_industry_province_city`  (
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分页链接',
  `flag` tinyint(1) NULL DEFAULT NULL COMMENT '是否爬过',
  PRIMARY KEY (`href`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for t_industry_province_city_qu
-- ----------------------------
DROP TABLE IF EXISTS `t_industry_province_city_qu`;
CREATE TABLE `t_industry_province_city_qu`  (
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分页链接',
  `flag` tinyint(1) NULL DEFAULT NULL COMMENT '是否爬过',
  PRIMARY KEY (`href`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;


-- ----------------------------
-- Table structure for t_industry_province_city_qu_page
-- ----------------------------
DROP TABLE IF EXISTS `t_industry_province_city_qu_page`;
CREATE TABLE `t_industry_province_city_qu_page`  (
  `href` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分页链接',
  `flag` tinyint(1) NULL DEFAULT NULL COMMENT '是否爬过',
  PRIMARY KEY (`href`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;