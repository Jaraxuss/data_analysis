create table house_info_log
(
    id                        int auto_increment comment '自增id' primary key,
    houseId                   varchar(255) comment '房源id',
    communityName             varchar(255) null comment '小区名称',
    region                    varchar(255) null comment '所在区域',
    totalPrice                float        null comment '总价（万元）',
    unitPrice                 float        null comment '单价（元/平米）',
    buildingArea              float        null comment '建筑面积',
    innerArea                 float        null comment '套内面积',
    houseType                 varchar(255) null comment '房屋户型',
    orientation               varchar(255) null comment '房屋朝向',
    floor                     varchar(255) null comment '所在楼层',
    houseStructure            varchar(255) null comment '户型结构',
    renovationCondition       varchar(255) null comment '装修情况',
    ladderHouseholdProportion varchar(255) null comment '梯户比例',
    hasElevator               varchar(255) null comment '配备电梯',
    buildingType              varchar(255) null comment '建筑类型',
    buildingStructure         varchar(255) null comment '建筑结构',
    yearOfPropertyRights      varchar(255) null comment '产权年限',
    tradingAuthority          varchar(255) null comment '交易权属',
    housingPurposes           varchar(255) null comment '房屋用途',
    yearOfHousing             varchar(255) null comment '房屋年限',
    propertyRights            varchar(255) null comment '产权所属',
    mortgageInfo              varchar(255) null comment '抵押信息',
    premisesPermitInfo        varchar(255) null comment '房本备件',
    href                      varchar(255) null comment '链接',
    listingAt                 bigint       null comment '挂牌时间',
    lastTransactionAt         bigint       null comment '上次交易',
    createdAt                 bigint       not null comment '创建时间'
)
    comment '二手房信息日志表';

create table house_analysis_entire
(
    id        int auto_increment comment '自增id' primary key,
    houseId   varchar(255) comment '房源id',
    delta     float  null comment '总变化量 第一次与最近一次价格差值',
    status    varchar(64) comment '状态（降价 down、涨价 up、新房 new）',
    downCount int    null comment '降价次数',
    upCount   int    null comment '涨价次数',
    createdAt bigint not null comment '创建时间'
)
    comment '整体分析表';

create table house_analysis_daily
(
    id        int auto_increment comment '自增id' primary key,
    houseId   varchar(255) comment '房源id',
    delta     float  null comment '较上一次变化量',
    status    varchar(64) comment '状态（降价 down、涨价 up、新房 new）',
    createdAt bigint not null comment '创建时间'
)
    comment '每日分析表';

create index idx_houseId_createdAt on house_info_log (houseId, createdAt);