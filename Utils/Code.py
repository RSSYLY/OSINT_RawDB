# 定义HTTP状态码
# 规范来自 https://pythondjango.cn/django/rest-framework/1-RESTfull-API-why-DRF/
# 成功代码
SUCCESS_CODE = 200  # 服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）

# 成功代码 - 创建或修改数据成功
SUCCESS_CREATED_CODE = 201  # 用户新建或修改数据成功

# 成功代码 - 异步任务已进入后台排队
SUCCESS_ACCEPTED_CODE = 202  # 表示一个请求已经进入后台排队（异步任务）

# 成功代码 - 用户删除数据成功
SUCCESS_NO_CONTENT_CODE = 204  # 用户删除数据成功

# 失败代码 - 无效请求
FAIL_CODE = 400  # 用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。

# 失败代码 - 未授权
FAIL_UNAUTHORIZED_CODE = 401  # 表示用户没有权限（令牌、用户名、密码错误）。

# 失败代码 - 访问被禁止
FAIL_FORBIDDEN_CODE = 403  # 表示用户得到授权（与401错误相对），但是访问是被禁止的。

# 失败代码 - 未找到项
ITEM_NOT_FOUND_CODE = 404  # 用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。

# 失败代码 - 请求格式不可得
FAIL_NOT_ACCEPTABLE_CODE = 406  # 用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。

# 失败代码 - 资源永久删除
FAIL_GONE_CODE = 410  # 用户请求的资源被永久删除，且不会再得到的。

# 失败代码 - 验证错误
FAIL_UNPROCESSABLE_ENTITY_CODE = 422  # 当创建一个对象时，发生一个验证错误。

# 服务器失败代码
SERVER_FAIL_CODE = 500  # 服务器发生错误
